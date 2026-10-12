#!/usr/bin/env python3
"""Builds the site from the text in content/.

Usage: python3 build.py

Output for each language (prefix "" for English, "ko/", "ja/"):
  <prefix>index.html                    first page
  <prefix>projects/<slug>/index.html    one page per project part
Links are root-relative, so preview with a server whose root is this folder.
"""
import html
import os

from content import common as C
from content import home as HOME
from content import agent, anomaly, deployment, manipulation, perception

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = {m.PAGE["slug"]: m.PAGE for m in (perception, anomaly, deployment, agent, manipulation)}
CUR = ' aria-current="page"'


def project_of(slug):
    for p in C.PROJECTS:
        for i, (s, _title, _desc) in enumerate(p["pages"]):
            if s == slug:
                return p, i
    raise KeyError(slug)


def page_label(slug):
    """'Project 1-2' for a part of project 1, 'Project 2' for a single-page project."""
    p, i = project_of(slug)
    return f'Project {p["no"]}-{i + 1}' if len(p["pages"]) > 1 else f'Project {p["no"]}'


class Site:
    def __init__(self, lang, prefix):
        self.lang = lang
        self.prefix = prefix

    # ---- small helpers
    def t(self, x):
        if x is None:
            return ""
        return x[self.lang] if isinstance(x, dict) else x

    def e(self, x):
        return html.escape(self.t(x), quote=False)

    def attr(self, x):
        return html.escape(self.t(x), quote=True)

    def home_url(self, anchor=""):
        return f"/{self.prefix}{anchor}"

    def page_url(self, slug):
        return f"/{self.prefix}projects/{slug}/"

    def status(self, keys):
        if not keys:
            return ""
        parts = [
            f'<span class="st{" op" if k in C.OP_KEYS else ""}">{self.e(C.STATUS[k])}</span>'
            for k in keys
        ]
        return '<span class="status">' + '<span class="sep"> / </span>'.join(parts) + "</span>"

    def cell(self, x):
        if isinstance(x, tuple) and x and x[0] == "st":
            return self.status(x[1])
        return self.e(x)

    # ---- page frame
    def head(self, title, description, path):
        alternates = "".join(
            f'<link rel="alternate" hreflang="{code}" href="{C.SITE_URL}{pfx}{path}">'
            for code, _, pfx in C.LANGS
        ) + f'<link rel="alternate" hreflang="x-default" href="{C.SITE_URL}{path}">'
        return f"""<!doctype html>
<html lang="{self.lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<link rel="canonical" href="{C.SITE_URL}{self.prefix}{path}">
{alternates}
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(description, quote=True)}">
<meta property="og:url" content="{C.SITE_URL}{self.prefix}{path}">
<link rel="stylesheet" href="/styles.css">
</head>
<body class="lang-{self.lang}">
"""

    def top(self, nav_html, path):
        switch = "".join(
            f'<a href="/{pfx}{path}" lang="{code}" hreflang="{code}"{CUR if code == self.lang else ""}>{label}</a>'
            for code, label, pfx in C.LANGS
        )
        return f"""<header class="top">
  <div class="wrap top-inner">
    <a class="brand" href="{self.home_url()}">{self.e(C.NAME)}</a>
    <nav class="nav" aria-label="Sections">{nav_html}</nav>
    <nav class="langs" aria-label="Language">{switch}</nav>
  </div>
</header>
"""

    def foot(self):
        return (
            f'<footer class="wrap foot"><span>{self.e(C.NAME)}</span><span>{C.TITLE}</span></footer>\n'
            "</body>\n</html>\n"
        )

    # ---- diagrams
    def legend(self, kinds):
        items = []
        if "judge" in kinds:
            items.append(f'<span><i class="k-judge"></i>{self.e(C.UI["legend_judge"])}</span>')
        if "fail" in kinds:
            items.append(f'<span><i class="k-fail"></i>{self.e(C.UI["legend_fail"])}</span>')
        return f'<p class="legend">{"".join(items)}</p>' if items else ""

    def flow_list(self, steps, cls="flow"):
        items = []
        for title, sub, kind in steps:
            sub_html = f"<span>{self.e(sub)}</span>" if sub else ""
            k = f' class="k-{kind}"' if kind else ""
            items.append(f"<li{k}><strong>{self.e(title)}</strong>{sub_html}</li>")
        n = len(steps)
        cols = {5: 5, 6: 3, 7: 4, 8: 4}.get(n, min(n, 4))
        return f'<ol class="{cls}" style="--cols:{cols}">' + "".join(items) + "</ol>"

    def flow(self, caption, steps, note):
        kinds = {k for _, _, k in steps if k}
        note_html = f'<p class="note">{self.e(note)}</p>' if note else ""
        return (
            '<figure class="diagram">'
            f"<figcaption>{self.e(caption)}</figcaption>"
            f"{self.flow_list(steps)}{self.legend(kinds)}{note_html}"
            "</figure>"
        )

    def node(self, title, sub, kind=None):
        k = f" k-{kind}" if kind else ""
        return f'<div class="node{k}"><strong>{self.e(title)}</strong><span>{self.e(sub)}</span></div>'

    def io(self, d):
        ins = "".join(self.node(a, b) for a, b in d["inputs"])
        outs = "".join(self.node(a, b) for a, b in d["outputs"])
        nodes = "".join(self.node(a, b, k) for a, b, k in d["nodes"])
        shared = f'<div class="io-shared">{self.node(*d["shared"])}</div>' if d.get("shared") else ""
        base = f'<div class="io-base">{self.node(*d["base"])}</div>' if d.get("base") else ""
        kinds = {k for _, _, k in d["nodes"] if k}
        note_html = f'<p class="note">{self.e(d["note"])}</p>' if d.get("note") else ""
        return (
            '<figure class="diagram">'
            f'<figcaption>{self.e(d["caption"])}</figcaption>'
            '<div class="io">'
            f'<div class="io-col">{ins}</div>'
            '<div class="io-arrow" aria-hidden="true"></div>'
            '<div class="io-core">'
            f'<p class="io-title">{self.e(d["core_title"])}</p>'
            f'<div class="io-nodes" style="--cols:{len(d["nodes"])}">{nodes}</div>'
            f"{shared}{base}"
            "</div>"
            '<div class="io-arrow" aria-hidden="true"></div>'
            f'<div class="io-col">{outs}</div>'
            "</div>"
            f"{self.legend(kinds)}{note_html}"
            "</figure>"
        )

    def tree(self, d):
        children = "".join(self.node(a, b) for a, b in d["children"])
        note_html = f'<p class="note">{self.e(d["note"])}</p>' if d.get("note") else ""
        return (
            '<figure class="diagram structure">'
            f'<figcaption>{self.e(d["caption"])}</figcaption>'
            f'<div class="node top-node"><strong>{self.e(d["top"][0])}</strong><span>{self.e(d["top"][1])}</span></div>'
            f'<div class="link"><span>{self.e(d["link"])}</span></div>'
            f'<div class="children">{children}</div>'
            f"{note_html}"
            "</figure>"
        )

    def table(self, head, rows, opts=None):
        opts = opts or {}
        heads = [self.t(h) for h in head]
        thead = "".join(
            f'<th scope="col"{" class=" + chr(34) + "c-judge-h" + chr(34) if opts.get("judge_col") == c else ""}>{html.escape(h)}</th>'
            for c, h in enumerate(heads)
        )
        body = []
        for r, row in enumerate(rows):
            cells = []
            for c, x in enumerate(row):
                label = html.escape(heads[c], quote=True)
                cls = ' class="c-judge"' if opts.get("judge_col") == c else ""
                if c == 0 and opts.get("first_bold"):
                    cells.append(f'<th scope="row" data-label="{label}">{self.cell(x)}</th>')
                else:
                    cells.append(f'<td data-label="{label}"{cls}>{self.cell(x)}</td>')
            row_cls = ' class="r-fail"' if r in opts.get("fail_rows", []) else ""
            body.append(f"<tr{row_cls}>{''.join(cells)}</tr>")
        return (
            f'<table class="grid cols-{len(heads)}{" " + opts["cls"] if opts.get("cls") else ""}"><thead><tr>{thead}</tr></thead>'
            f"<tbody>{''.join(body)}</tbody></table>"
        )

    def scenario(self, d):
        kinds = {k for _, _, k in d["strip"] if k}
        rows = "".join(f'<tr><th scope="row">{self.e(a)}</th><td>{self.e(b)}</td></tr>' for a, b in d["rows"])
        request = (
            f'<p class="request"><span>{self.e(C.UI["request"])}</span>{self.e(d["request"])}</p>'
            if d.get("request") else ""
        )
        note_html = f'<p class="note">{self.e(d["note"])}</p>' if d.get("note") else ""
        return (
            '<article class="scenario">'
            f'<div class="item-head"><h3>{self.e(d["title"])}</h3>{self.status(d["status"])}</div>'
            f"{request}"
            f'{self.flow_list(d["strip"], "flow strip")}{self.legend(kinds)}'
            f'<table class="steps"><tbody>{rows}</tbody></table>'
            f"{note_html}"
            "</article>"
        )

    def links(self, items):
        lis = []
        for slug, desc in items:
            p, i = project_of(slug)
            lis.append(
                f'<li><a href="{self.page_url(slug)}"><span class="lbl">{page_label(slug)}</span>'
                f'{html.escape(p["pages"][i][1])}</a><span>{self.e(desc)}</span></li>'
            )
        return f'<ul class="links">{"".join(lis)}</ul>'

    def block(self, b):
        kind = b[0]
        if kind == "h2":
            return f'<h2 id="{b[1]}">{self.e(C.H[b[1]])}</h2>'
        if kind == "h3":
            return f'<div class="item-head sub"><h3>{self.e(b[1])}</h3>{self.status(b[2])}</div>'
        if kind == "p":
            return f"<p>{self.e(b[1])}</p>"
        if kind == "note":
            return f'<p class="note boxed">{self.e(b[1])}</p>'
        if kind == "points":
            lis = "".join(f"<li><strong>{self.e(a)}</strong><span>{self.e(c)}</span></li>" for a, c in b[1])
            return f'<ol class="points">{lis}</ol>'
        if kind == "table":
            return self.table(b[1], b[2], b[3] if len(b) > 3 else {})
        if kind == "flow":
            return self.flow(b[1], b[2], b[3])
        if kind == "io":
            return self.io(b[1])
        if kind == "tree":
            return self.tree(b[1])
        if kind == "scenario":
            return self.scenario(b[1])
        if kind == "links":
            return self.links(b[1])
        raise ValueError(kind)

    # ---- detail page
    def detail(self, page):
        slug = page["slug"]
        proj, idx = project_of(slug)
        path = f"projects/{slug}/"
        n = len(proj["pages"])
        out = [self.head(f'{page["title"]} | {self.t(C.NAME)}', self.t(page["claim"]), path)]
        nav = f'<a href="{self.home_url("#projects")}">{self.e(C.UI["all_projects"])}</a>'
        out.append(self.top(nav, path))

        crumb = [f'Project {proj["no"]}', html.escape(proj["title"])]
        parts = ""
        if n > 1:
            crumb.append(self.t(C.UI["part_of"]).format(i=idx + 1, n=n))
            tabs = "".join(
                f'<a href="{self.page_url(s)}"{CUR if s == slug else ""}>'
                f'<span class="lbl">{proj["no"]}-{i + 1}</span>{html.escape(tt)}</a>'
                for i, (s, tt, _) in enumerate(proj["pages"])
            )
            parts = f'<nav class="parts" aria-label="Parts">{tabs}</nav>'
        out.append(
            '<div class="where"><div class="wrap">'
            f'<p class="crumb">{" · ".join(crumb)}</p>{parts}'
            "</div></div>\n"
        )

        facts = "".join(f"<div><dt>{self.e(C.UI[k])}</dt><dd>{self.cell(v)}</dd></div>" for k, v in page["facts"])
        toc = "".join(f'<a href="#{b[1]}">{self.e(C.H[b[1]])}</a>' for b in page["blocks"] if b[0] == "h2")
        video = page.get("video")  # set "video": "assets/<file>" in the page to show a demo video
        media = (
            f'<figure class="media"><video controls preload="metadata" src="/{video}"></video></figure>'
            if video else '<figure class="media" hidden></figure>'
        )
        out.append(
            '<main class="wrap detail">\n'
            f'<p class="kicker">{page_label(slug)}</p>'
            f'<h1>{html.escape(page["title"])}</h1>'
            f'<p class="claim">{self.e(page["claim"])}</p>'
            f'<dl class="facts">{facts}</dl>'
            f'<nav class="toc" aria-label="{self.attr(C.UI["on_this_page"])}">{toc}</nav>'
            f"{media}\n"
        )
        out.append("\n".join(self.block(b) for b in page["blocks"]))

        order = C.PAGE_ORDER
        k = order.index(slug)
        pager = []
        for step, key in ((-1, "prev"), (1, "next")):
            j = k + step
            if 0 <= j < len(order):
                s2 = order[j]
                p2, i2 = project_of(s2)
                pager.append(
                    f'<a class="{key}" href="{self.page_url(s2)}"><span>{self.e(C.UI[key])} · {page_label(s2)}</span>'
                    f'{html.escape(p2["pages"][i2][1])}</a>'
                )
            else:
                pager.append(
                    f'<a class="{key}" href="{self.home_url("#projects")}"><span>{self.e(C.UI[key])}</span>'
                    f'{self.e(C.UI["all_projects"])}</a>'
                )
        out.append(f'\n<nav class="pager">{"".join(pager)}</nav>\n</main>\n')
        out.append(self.foot())
        return "".join(out)

    # ---- first page
    def home(self):
        H = HOME
        out = [self.head(f"{self.t(C.NAME)} | {C.TITLE}", self.t(H.META_DESCRIPTION), "")]
        nav = "".join(
            f'<a href="#{i}">{label}</a>'
            for i, label in (("system", "System"), ("projects", "Projects"), ("connections", "Connections"),
                             ("experience", "Experience"), ("skills", "Skills"), ("contact", "Contact"))
        )
        out.append(self.top(nav, ""))
        sep = "" if self.lang == "ja" else " "
        out.append(f"""<main id="top" class="wrap">
<section class="intro">
  <div class="intro-text">
    <h1>{self.e(C.NAME)}</h1>
    <p class="role">{C.TITLE}</p>
    <p class="summary">{sep.join(self.e(s) for s in H.INTRO)}</p>
    <dl class="facts">
      <div><dt>Location</dt><dd>{H.LOCATION}</dd></div>
      <div><dt>Languages</dt><dd>{self.e(H.LANGUAGES)}</dd></div>
      <div><dt>Contact</dt><dd><a href="mailto:{C.EMAIL}">{C.EMAIL}</a> · <a href="{C.LINKEDIN}" rel="noopener">LinkedIn</a></dd></div>
    </dl>
  </div>
  <img class="photo" src="/{C.PHOTO}" alt="{self.attr(C.NAME)}" width="487" height="684">
</section>
<section id="purpose">
  <h2>{self.e(H.PURPOSE_TITLE)}</h2>
  {"".join(f"<p>{self.e(p)}</p>" for p in H.PURPOSE)}
</section>
""")

        rows = []
        for layer, role, keys, pages in H.SYSTEM_MAP:
            links = "".join(f'<a href="{self.page_url(s)}">{label}</a>' for s, label in pages)
            rows.append(
                f'<tr><th scope="row" data-label="Layer">{html.escape(layer)}</th>'
                f'<td data-label="Role">{self.e(role)}</td>'
                f'<td data-label="Status">{self.status(keys)}</td>'
                f'<td data-label="{self.attr(H.SYSTEM_HEAD[3])}" class="go">{links}</td></tr>'
            )
        out.append(f"""<section id="system">
  <h2>{self.e(H.SYSTEM_TITLE)}</h2>
  <p class="lead">{self.e(H.SYSTEM_INTRO)} {self.e(C.STATUS_LEGEND)}</p>
  <table class="grid cols-4 map"><thead><tr>{"".join(f'<th scope="col">{self.e(h)}</th>' for h in H.SYSTEM_HEAD)}</tr></thead>
  <tbody>{"".join(rows)}</tbody></table>
</section>
""")

        cards = []
        for p in C.PROJECTS:
            meta = [f'<span class="who">{self.e(p["role"])}</span>', self.e(p["period"])]
            if p.get("scale"):
                meta.append(self.status(p["scale"]))
            if p.get("scale_text"):
                meta.append(self.e(p["scale_text"]))
            if len(p["pages"]) > 1:
                items = "".join(
                    f'<li><a href="{self.page_url(s)}"><span class="lbl">{p["no"]}-{i + 1}</span>{html.escape(tt)}</a>'
                    f"<span>{self.e(desc)}</span></li>"
                    for i, (s, tt, desc) in enumerate(p["pages"])
                )
                more = f'<ul class="links in-card">{items}</ul>'
            else:
                s = p["pages"][0][0]
                more = f'<p class="more"><a href="{self.page_url(s)}">{self.e(C.UI["read"])}: Project {p["no"]} →</a></p>'
            cards.append(
                f'<article class="card" id="project-{p["no"]}">'
                f'<p class="kicker">Project {p["no"]}</p>'
                f'<h3>{html.escape(p["title"])}</h3>'
                f'<p class="meta">{" · ".join(meta)}</p>'
                f'<p>{self.e(p["summary"])}</p>'
                f"{more}"
                "</article>"
            )
        out.append(f"""<section id="projects">
  <h2>{self.e(H.PROJECTS_TITLE)}</h2>
  <p class="lead">{self.e(H.PROJECTS_INTRO)}</p>
  {"".join(cards)}
</section>
<section id="connections">
  <h2>{self.e(H.CONNECT_TITLE)}</h2>
  <p class="lead">{self.e(H.CONNECT_INTRO)}</p>
  {self.table(H.CONNECT_HEAD, [[a, b, ("st", k)] for a, b, k in H.CONNECTIONS], {"first_bold": True, "cls": "conn"})}
</section>
""")

        jobs = "".join(
            '<article class="job">'
            f'<div class="item-head"><h3>{self.e(j["org"])} <span class="sub">| {self.e(j["role"])}</span></h3>'
            f'<span class="date">{self.e(j["period"])}</span></div>'
            f'<ul class="plain">{"".join(f"<li>{self.e(line)}</li>" for line in j["lines"])}</ul>'
            "</article>"
            for j in H.EXPERIENCE
        )
        ed = H.EDUCATION
        out.append(f"""<section id="experience">
  <h2>{H.EXPERIENCE_TITLE}</h2>
  {jobs}
  <h2 class="second">{H.EDUCATION_TITLE}</h2>
  <article class="job">
    <div class="item-head"><h3>{self.e(ed["org"])} <span class="sub">| {self.e(ed["role"])}</span></h3><span class="date">{self.e(ed["period"])}</span></div>
  </article>
</section>
<section id="skills">
  <h2>{H.SKILLS_TITLE}</h2>
  <dl class="skills">{"".join(f"<div><dt>{self.e(a)}</dt><dd>{self.e(b)}</dd></div>" for a, b in H.SKILLS)}</dl>
</section>
<section id="contact">
  <h2>{H.CONTACT_TITLE}</h2>
  <p class="lead">{self.e(H.CONTACT_INTRO)}</p>
  <ul class="contact">
    <li><span>Email</span><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>
    <li><span>LinkedIn</span><a href="{C.LINKEDIN}" rel="noopener">linkedin.com/in/junho-kim-a3ba8a2aa</a></li>
  </ul>
</section>
</main>
""")
        out.append(self.foot())
        return "".join(out)


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    count = 0
    for code, _, prefix in C.LANGS:
        site = Site(code, prefix)
        write(f"{prefix}index.html", site.home())
        count += 1
        for slug in C.PAGE_ORDER:
            write(f"{prefix}projects/{slug}/index.html", site.detail(PAGES[slug]))
            count += 1
    # GitHub Pages serves the files as they are, without Jekyll.
    open(os.path.join(ROOT, ".nojekyll"), "a").close()
    print(f"wrote {count} pages")


if __name__ == "__main__":
    main()
