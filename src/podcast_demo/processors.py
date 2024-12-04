from pathlib import Path

from feedgen.feed import FeedGenerator
from sphinx.application import Sphinx

from . import models


def generate_podcast_feed(app: Sphinx, exc: Exception | None = None):
    if exc:
        print("Cancelled")
        raise exc
    feed = models.Feed.init(app)
    for docname in app.env.all_docs.keys():
        try:
            entry = models.generate_entry(app, docname)
            if entry:
                feed.entries.append(entry)
        except ValueError:
            continue
    fg = FeedGenerator()
    fg.load_extension("podcast")
    fg.language("ja")
    fg.id(feed.link)
    fg.title(feed.title)
    fg.link(href=feed.link, rel="alternate")
    fg.description("Demo")
    for entry in feed.entries:
        fg_entry = fg.add_entry()
        fg_entry.id(entry.link)
        fg_entry.link(href=entry.link)
        fg_entry.title(entry.title)
        fg_entry.description(entry.summary)
        fg_entry.pubDate(entry.updated.strftime("%a, %d %b %Y %H:%M:%S +0900"))
        fg_entry.enclosure(
            entry.media_url,
            type="audio/mp3",
            length=entry.media_realpath.stat().st_size,
        )
    out_path = Path(app.outdir) / "podcast.xml"
    fg.rss_file(out_path, pretty=True)
