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
    fg.id(feed.link)
    fg.title(feed.title)
    fg.link(href=feed.link, rel="alternate")
    fg.description("sss")
    for entry in feed.entries:
        print(type(entry))
        fg_entry = fg.add_entry()
        fg_entry.id(entry.link)
        fg_entry.link(href=entry.link)
        fg_entry.title(entry.title)
        fg_entry.description(entry.summary)
        fg_entry.enclosure(entry.media)
    out_path = Path(app.outdir) / "podcast.xml"
    print(out_path)
    fg.rss_file(out_path)
