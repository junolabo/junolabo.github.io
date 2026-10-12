#!/usr/bin/env python3
"""Builds index.html, ko/index.html and ja/index.html from content.py.

Usage: python3 build.py
"""
import html
import os

import content as C

ROOT = os.path.dirname(os.path.abspath(__file__))
OP_KEYS = {"op", "op_inhouse"}


def render(lang, here):
    # `here` is this page's path under the site root ("" or "ko/").
    up = "../" if here else ""

    def t(x):
        if x is None:
            return ""
        return x[lang] if isinstance(x, dict) else x

    def e(x):
        s = html.escape(t(x), quote=False)
        return s.replace("{{b}}", "<strong>").replace("{{/b}}", "</strong>")

    def status(keys):
        if not keys:
            return ""
        parts = [
            f'<span class="st{" op" if k in OP_KEYS else ""}">{e(C.STATUS[k])}</span>'
            for k in keys
        ]
        return '<span class="status">' + '<span class="sep"> / </span>'.join(parts) + "</span>"

    def flow(steps, cls="flow"):
        items = []
        for title, sub in steps:
            sub_html = f"<span>{e(sub)}</span>" if sub else ""
            items.append(f"<li><strong>{e(title)}</strong>{sub_html}</li>")
        n = len(steps)
        cols = {6: 3, 5: 3}.get(n, min(n, 4))
        return f'<ol class="{cls}" style="--cols:{cols}">' + "".join(items) + "</ol>"

    def diagram(d):
        note = f'<p class="note">{e(d["note"])}</p>' if d.get("note") else ""
        return (
            '<figure class="diagram">'
            f'<figcaption>{e(d["caption"])}</figcaption>'
            f'{flow(d["steps"])}{note}'
            "</figure>"
        )

    def media(p):
        # The slot stays hidden until a video file is set in content.py.
        if not p.get("video"):
            return f'<figure class="media" id="video-{p["id"]}" hidden></figure>'
        return (
            f'<figure class="media" id="video-{p["id"]}">'
            f'<video controls preload="metadata" src="{up}{p["video"]}"></video>'
            "</figure>"
        )

    # ---- head
    alternates = "".join(
        f'<link rel="alternate" hreflang="{code}" href="{C.SITE_URL}{path}">'
        for code, _, path in C.LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{C.SITE_URL}">'
    page_title = f"{t(C.NAME)} | {C.TITLE}"
    head = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(page_title)}</title>
<meta name="description" content="{html.escape(t(C.META_DESCRIPTION), quote=True)}">
<link rel="canonical" href="{C.SITE_URL}{here}">
{alternates}
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(page_title, quote=True)}">
<meta property="og:description" content="{html.escape(t(C.META_DESCRIPTION), quote=True)}">
<meta property="og:url" content="{C.SITE_URL}{here}">
<link rel="stylesheet" href="{up}styles.css">
</head>
<body class="lang-{lang}">
"""

    # ---- header
    nav = "".join(f'<a href="#{i}">{label}</a>' for i, label in C.NAV)
    switch = "".join(
        f'<a href="{up}{path or "./"}" lang="{code}" hreflang="{code}"'
        f'{" aria-current=" + chr(34) + "page" + chr(34) if code == lang else ""}>{label}</a>'
        for code, label, path in C.LANGS
    )
    header = f"""<header class="top">
  <div class="wrap top-inner">
    <a class="brand" href="#top">{e(C.NAME)}</a>
    <nav class="nav" aria-label="Sections">{nav}</nav>
    <nav class="langs" aria-label="Language">{switch}</nav>
  </div>
</header>
<main id="top" class="wrap">
"""

    # ---- intro
    summary = ("" if lang == "ja" else " ").join(e(s) for s in C.SUMMARY)
    intro = f"""<section class="intro">
  <div class="intro-text">
    <h1>{e(C.NAME)}</h1>
    <p class="role">{e(C.TITLE)}</p>
    <p class="summary">{summary}</p>
    <dl class="facts">
      <div><dt>Location</dt><dd>{e(C.LOCATION)}</dd></div>
      <div><dt>{e(C.LANGUAGES_LABEL)}</dt><dd>{e(C.LANGUAGES)}</dd></div>
      <div><dt>Contact</dt><dd><a href="mailto:{C.EMAIL}">{C.EMAIL}</a> · <a href="{C.LINKEDIN}" rel="noopener">LinkedIn</a></dd></div>
    </dl>
  </div>
  <img class="photo" src="{up}{C.PHOTO}" alt="{html.escape(t(C.NAME), quote=True)}" width="487" height="684">
</section>
"""

    # ---- system
    rows = "".join(
        f"<tr><th scope=\"row\">{e(layer)}</th><td>{e(role)}</td><td>{status(keys)}</td></tr>"
        for layer, role, keys in C.SYSTEM_MAP
    )
    s = C.STRUCTURE
    children = "".join(
        f'<div class="node"><strong>{e(a)}</strong><span>{e(b)}</span></div>' for a, b in s["children"]
    )
    system = f"""<section id="system">
  <h2>System</h2>
  <p class="lead">{e(C.SYSTEM_INTRO)}</p>
  <table class="map">
    <thead><tr>{"".join(f"<th scope='col'>{h}</th>" for h in C.SYSTEM_MAP_HEAD)}</tr></thead>
    <tbody>{rows}</tbody>
  </table>
  <figure class="diagram structure">
    <figcaption>{e(s["caption"])}</figcaption>
    <div class="node top-node"><strong>{e(s["top"][0])}</strong><span>{e(s["top"][1])}</span></div>
    <div class="link"><span>{e(s["link"])}</span></div>
    <div class="children">{children}</div>
    <div class="inside">
      <p class="inside-label">{e(s["inside_label"])}</p>
      {flow([(x, None) for x in s["inside"]])}
    </div>
    <p class="note">{e(s["note"])}</p>
  </figure>
</section>
"""

    # ---- work
    projects = []
    for n, p in enumerate(C.PROJECTS, 1):
        meta = [f'<span class="who">{e(p["role"])}</span>', e(p["period"])]
        if p.get("scale"):
            meta.append(f'<span class="st{" op" if p["scale_op"] else ""}">{e(p["scale"])}</span>')
        groups = []
        for label, items in p["groups"]:
            lis = "".join(
                "<li>"
                f'<div class="item-head"><h5>{e(name)}</h5>{status(keys)}</div>'
                f"<p>{e(text)}</p>"
                "</li>"
                for name, keys, text in items
            )
            head_html = f'<h4 class="group">{e(label)}</h4>' if label else ""
            groups.append(f'{head_html}<ul class="items">{lis}</ul>')
        projects.append(
            f'<article class="project" id="{p["id"]}">'
            f'<h3><span class="no">{n}</span>{e(p["title"])}</h3>'
            f'<p class="meta">{" · ".join(meta)}</p>'
            f'<p class="context">{e(p["context"])}</p>'
            f"{media(p)}"
            f'{"".join(groups)}'
            f'{diagram(p["diagram"])}'
            "</article>"
        )
    work = f"""<section id="work">
  <h2>Work</h2>
  <p class="lead">{e(C.WORK_INTRO)}</p>
  {"".join(projects)}
</section>
"""

    # ---- scenarios
    cards = []
    for sc in C.SCENARIOS:
        steps = "".join(
            f"<li><strong>{e(who)}</strong><span>{e(what)}</span></li>" for who, what in sc["steps"]
        )
        note = f'<p class="note">{e(sc["note"])}</p>' if sc.get("note") else ""
        cards.append(
            '<article class="scenario">'
            f'<div class="item-head"><h3>{e(sc["title"])}</h3>{status(sc["status"])}</div>'
            f'<p class="request">{e(sc["request"])}</p>'
            f'<ol class="steps">{steps}</ol>{note}'
            "</article>"
        )
    scenarios = f"""<section id="scenarios">
  <h2>Scenarios</h2>
  <p class="lead">{e(C.SCENARIOS_INTRO)}</p>
  {"".join(cards)}
</section>
"""

    # ---- experience, education
    jobs = "".join(
        '<article class="job">'
        f'<div class="item-head"><h3>{e(j["org"])} <span class="sub">| {e(j["role"])}</span></h3>'
        f'<span class="date">{e(j["period"])}</span></div>'
        f'<ul class="plain">{"".join(f"<li>{e(line)}</li>" for line in j["lines"])}</ul>'
        "</article>"
        for j in C.EXPERIENCE
    )
    ed = C.EDUCATION
    experience = f"""<section id="experience">
  <h2>Experience</h2>
  {jobs}
  <h2 class="second">Education</h2>
  <article class="job">
    <div class="item-head"><h3>{e(ed["org"])} <span class="sub">| {e(ed["role"])}</span></h3><span class="date">{e(ed["period"])}</span></div>
  </article>
</section>
"""

    # ---- skills
    skills = f"""<section id="skills">
  <h2>Skills</h2>
  <dl class="skills">{"".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in C.SKILLS)}</dl>
</section>
"""

    # ---- contact
    contact = f"""<section id="contact">
  <h2>Contact</h2>
  <p class="lead">{e(C.CONTACT_INTRO)}</p>
  <ul class="contact">
    <li><span>Email</span><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></li>
    <li><span>LinkedIn</span><a href="{C.LINKEDIN}" rel="noopener">linkedin.com/in/junho-kim-a3ba8a2aa</a></li>
  </ul>
</section>
</main>
<footer class="wrap foot"><span>{e(C.FOOTER)}</span><span>{C.TITLE}</span></footer>
</body>
</html>
"""
    return head + header + intro + system + work + scenarios + experience + skills + contact


def main():
    for code, _, path in C.LANGS:
        out_dir = os.path.join(ROOT, path)
        os.makedirs(out_dir, exist_ok=True)
        out = os.path.join(out_dir, "index.html")
        with open(out, "w", encoding="utf-8") as f:
            f.write(render(code, path))
        print("wrote", os.path.relpath(out, ROOT))
    # GitHub Pages serves the files as they are, without Jekyll.
    open(os.path.join(ROOT, ".nojekyll"), "a").close()


if __name__ == "__main__":
    main()
