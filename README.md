# Youtube itag collection

A collection of Youtube's itags - available in [Markdown, CSV and JSON](https://github.com/leonbrandt/yt-itag/releases/latest)

---

Youtube uses itags to identify formats of videos. Knowing them can be helpful for selecting the right format when downloading videos. The goal of this repository is to provide an up-to-date collection of all itags in convenient formats.

## Important to know

Itags don't always describe formats consistently. Learn about possible problems [here](docs.md).

## Contributing

Edit [data.md](data.md) and provide links to Youtube videos that confirm your changes with your pull request. Thank you!

## Building

If you want to generate a CSV or JSON-version by yourself run: (You will need python 3.5+)

```
pip install -r requirements.txt
python build.py
```
