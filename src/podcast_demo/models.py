from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from atsphinx.feed import models as feed_models
from atsphinx.audioplayer.nodes import audio
from sphinx.application import Sphinx


@dataclass
class Entry(feed_models.Entry):
    """Data for entry in Atom feed."""

    media: str


@dataclass
class Feed(feed_models.Feed):
    entries: list[Entry]


def generate_entry(app: Sphinx, docname: str) -> Entry | None:
    entry_base = feed_models.generate_entry(app, docname)
    doctree = app.env.get_doctree(docname)
    builder = app.builder
    audio_candicates = list(doctree.findall(audio))
    if not audio_candicates:
        return None
    audio_ = audio_candicates[0]
    uri = audio_["uri"]
    if uri in builder.images:
        audio_uri = Path(builder.imgpath) / quote(builder.images[uri])
        audio_url = Path(app.config.html_baseurl) / audio_uri
        return Entry(**asdict(entry_base), media=str(audio_url))
