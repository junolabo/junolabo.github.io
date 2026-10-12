# junolabo.github.io

Portfolio site of Junho Kim. Three languages, one page each.

| Page | Path |
| --- | --- |
| English | `/` |
| Korean | `/ko/` |
| Japanese | `/ja/` |

## Edit and build

All text lives in `content.py`. Each sentence is written once per language with `L(en, ko, ja)`.

```bash
python3 build.py
```

`build.py` writes `index.html`, `ko/index.html`, and `ja/index.html`. Do not edit those three files by hand.

## Demo videos

Each project has a hidden video slot. To show a video, put the file under `assets/` and set `"video"` of that project in `content.py`, for example `"video": "assets/perception.mp4"`. Then run the build.

## Local preview

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/`.

## Deploy

Push `main` to `origin`. GitHub Pages serves this repository at `https://junolabo.github.io`.
