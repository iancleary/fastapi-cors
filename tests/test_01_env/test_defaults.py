
from fastapi_cors.env import ALLOW_ORIGINS
from fastapi_cors.env import ALLOWED_CREDENTIALS
from fastapi_cors.env import ALLOWED_HEADERS
from fastapi_cors.env import ALLOWED_METHODS
from fastapi_cors.env import HOST
from fastapi_cors.env import PORT
from fastapi_cors.env import LOG_LEVEL


def test_allow_credentials() -> None:
    assert ALLOWED_CREDENTIALS is True


def test_allow_headers() -> None:
    assert ALLOWED_HEADERS == ["Access-Control-Allow-Origin"]


def test_allow_methods() -> None:
    assert ALLOWED_METHODS == ["*"]


def test_allow_origins() -> None:
    assert ALLOW_ORIGINS == [
        "http://localhost",
        "http://localhost:3000",
    ]


def test_host() -> None:
    assert HOST == "0.0.0.0"


def test_port() -> None:
    assert PORT == 8000


def test_log_level() -> None:
    assert LOG_LEVEL == "info"
