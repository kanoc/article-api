from fastapi.testclient import TestClient
from pytest_httpx import HTTPXMock

from api.web import app

from tests.web import client


def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200


def test_redoc():
    response = client.get("/redoc")
    assert response.status_code == 200


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "Zed is *not* dead"}


def test_articles(httpx_mock: HTTPXMock):
    test_article = {
        "title": "Test title",
        "description": "Dummy description",
        "content": "Dummy content",
        "url": "https://test.com",
        "image": "https://testimage.com",
        "publishedAt": "2022-10-23T13:00:40Z",
        "source": {
            "name": "Test source",
            "url": "https://testsourceimage.com"
        }
    }
    httpx_mock.add_response(method="GET", json={"articles": [test_article]})

    with TestClient(app) as client_with_event_handlers:
        response = client_with_event_handlers.get("/api/articles?keywords=test")
    assert response.status_code == 200
    articles = response.json()
    assert len(articles) == 1
    assert articles[0]["title"] == test_article["title"]
