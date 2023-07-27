"""Litestar template application.

.. todo:: Refactor routes into separate file
"""

from asyncio import sleep
from typing import Any

from dotenv import load_dotenv
from litestar import Controller, Litestar, Request, get
from litestar.response import Template
from litestar.types import ControllerRouterHandler

from src.config import openapi, static_files, template

__all__ = (
    "ConcurrencyModelExamplesController",
    "WebsocketExamplesController",
    "home",
)

load_dotenv()


@get(path="/", operation_id="home", tags=["frontend:home"], status_code=200, include_in_schema=False)
async def home(request: Request) -> Template:
    """Index page.

    Args:
        request: Request object

    Returns:
        Tuple: Response and status code
    """
    request.logger.info("Index page requested.")
    context = {
        "request": request,
        "repo_url": "https://github.com/JacobCoffee/litestar-template",
        "railway_ref_url": "https://railway.app/template/zx1KGh?referralCode=BMcs0x",
    }
    return Template("index.html", context=context)


class ConcurrencyModelExamplesController(Controller):
    """Controller showcasing concurrency models."""

    tags = ["concurrency"]

    @get("/async", operation_id="async", tags=["concurrency:async"], include_in_schema=True)
    async def async_hello_world(self) -> dict[str, Any]:
        """Route Handler for asynchronous endpoint.

        Returns:
            dict[str, Any]: Response
        """
        await sleep(0.1)
        return {"endpoint": "asynchronous"}

    @get("/sync", sync_to_thread=False, operation_id="sync", tags=["concurrency:sync"], include_in_schema=True)
    def sync_hello_world(self) -> dict[str, Any]:
        """Route Handler for synchronous endpoint.

        Returns:
            dict[str, Any]: Response
        """
        return {"endpoint": "synchronous"}


class WebsocketExamplesController(Controller):
    """Controller showcasing websockets.

    .. todo:: Implement example
    """

    ...


routes: list[ControllerRouterHandler] = [
    home,
    ConcurrencyModelExamplesController,
]
"""List of routes."""

app = Litestar(
    route_handlers=[*routes],
    # --- Config
    template_config=template.config,
    openapi_config=openapi.config,
    static_files_config=static_files.config,
    # --- Lifecycle
    on_startup=[],
    on_shutdown=[],
)
