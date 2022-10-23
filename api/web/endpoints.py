from typing import List, Dict

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
import httpx

from api import config
from api.models import Article, Message


router = APIRouter()


@router.get("/healthcheck")
async def healthcheck() -> Dict[str, str]:
    """Am I alive?"""

    return {"status": "Zed is *not* dead"}


@router.get("/api/articles", response_model=List[Article], responses={503: {"model": Message}})
@cache(expire=60)
async def articles(
    keywords: str = Query(min_length=3, max_length=50,
                          title="Article keywords",
                          description="Search for articles with these keywords"),
    limit: int = 10
):
    """Search for articles by custom keywords."""

    # Build and send the request.
    url_params: Dict[str, str | int] = {
        "token": config.GNEWS_API_TOKEN,
        "max": limit,
        "q": keywords
    }

    async with httpx.AsyncClient(headers={"Accept-Encoding": "gzip"}) as client:
        resp = await client.get(url=config.GNEWS_SEARCH_URL, params=url_params)

    if resp.status_code != 200:
        # API call failed. Treat it as a "Service Unavailable" case.
        return JSONResponse(status_code=503, content={"message": str(resp.content)})

    # Interpret and transform the response.
    json_resp = resp.json()
    article_list = json_resp.get("articles", [])
    if articles:
        return [
            {
                "title": article["title"],
                "description": article["description"],
                "content": article["content"],
                "url": article["url"],
                "image_url": article["image"],
                "published_at": article["publishedAt"],
                "source": {
                    "name": article["source"]["name"],
                    "url": article["source"]["url"]
                }
            }
            for article in article_list
        ]

    # No articles found.
    return []

