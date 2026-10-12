# junolabo.github.io

Portfolio site of Junho Kim. Three languages. One first page and five project pages per language.

| Page | English | Korean | Japanese |
| --- | --- | --- | --- |
| First page | `/` | `/ko/` | `/ja/` |
| Project 1-1 Perception Runtime | `/projects/perception-runtime/` | `/ko/projects/perception-runtime/` | `/ja/projects/perception-runtime/` |
| Project 1-2 VLM Anomaly Detection | `/projects/anomaly-detection/` | `/ko/…` | `/ja/…` |
| Project 1-3 Deployment & Model Update | `/projects/deployment/` | `/ko/…` | `/ja/…` |
| Project 2 Agent System | `/projects/agent-system/` | `/ko/…` | `/ja/…` |
| Project 3 Manipulation Learning | `/projects/manipulation-learning/` | `/ko/…` | `/ja/…` |

The three projects have the same numbers, titles, roles, and periods as the resume. Project 1 is explained in three parts.

## Edit and build

All text lives in `content/`. Each sentence is written once per language with `L(en, ko, ja)`.

| File | Content |
| --- | --- |
| `content/common.py` | names, status labels, the project list, section headings |
| `content/home.py` | first page |
| `content/perception.py`, `anomaly.py`, `deployment.py`, `agent.py`, `manipulation.py` | one project page each |

```bash
python3 build.py
```

`build.py` writes every `index.html`. Do not edit the HTML files by hand.

A project page is a list of blocks: `h2`, `h3`, `p`, `note`, `points`, `table`, `flow`, `io`, `tree`, `scenario`, `links`. See `build.py` for how each block is drawn.

## Demo videos

Each project page has a hidden video slot. To show a video, put the file under `assets/` and add `"video": "assets/<file>"` to the `PAGE` of that project. Then run the build.

## Local preview

Links are root-relative, so the server root must be this folder.

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/`.

## Deploy

Push `main` to `origin`. GitHub Pages serves this repository at `https://junolabo.github.io`.
