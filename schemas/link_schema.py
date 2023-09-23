from pydantic import BaseModel, HttpUrl


class CreateLink(BaseModel):
    link: str


class LinkDetail(CreateLink):
    short_link: str


class LinkList(BaseModel):
    links: list[LinkDetail]