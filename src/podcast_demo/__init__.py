from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata

from . import processors


def setup(app: Sphinx) -> ExtensionMetadata:
    app.connect("build-finished", processors.generate_podcast_feed)
    return {}

