"""Template config."""
from __future__ import annotations

from pathlib import Path

from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig

config = TemplateConfig(
    directory=Path(__file__).parent.parent / "static" / "templates",
    engine=JinjaTemplateEngine,
)
"""Template config for app."""
