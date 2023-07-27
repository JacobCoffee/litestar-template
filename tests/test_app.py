from litestar.testing import TestClient

from src.app import app


def test_sync() -> None:
    with TestClient(app=app) as client:
        assert client.get("/sync").json() == {"endpoint": "synchronous"}


def test_async() -> None:
    with TestClient(app=app) as client:
        assert client.get("/async").json() == {"endpoint": "asynchronous"}
