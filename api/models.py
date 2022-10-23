import datetime

from pydantic import BaseModel, HttpUrl


class ArticleSource(BaseModel):
    name: str
    url: HttpUrl


class Article(BaseModel):
    title: str
    description: str
    content: str
    url: HttpUrl
    image_url: HttpUrl
    published_at: datetime.datetime
    source: ArticleSource


class Message(BaseModel):
    message: str
