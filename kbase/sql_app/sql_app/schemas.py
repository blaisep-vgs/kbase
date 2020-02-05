from enum import Enum

from datetime import date, datetime
from typing import List

from pydantic import BaseModel


class ArticleType(str, Enum):
    preprint = "preprint"
    postprint = "postprint"
    proceeding = "proceeding"


class Article(BaseModel):
    id: str
    version: str
    source: str
    journal: str
    article_type: ArticleType
    title: str
    publication_date: date
    update_date: date
    link: str
    doid: str = ""
    summary: str = ""
    authors: List[str] = []
    affiliations: List[str] = []
    language: str = ""
    keywords: List[str] = []
    references: List[str] = []

    class Config:
        orm_mode = True


class ArticleCreate(Article):
    pass


class ArticleUpdate(Article):
    pass


class UserRatingBase(BaseModel):
    pass


class UserRatingCreate(UserRatingBase):
    value: float


class UserRating(UserRatingBase):
    id: int
    article_id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserCreate):
    id: int
    created_date: datetime
    last_login: datetime
    is_active: bool
    ratings: List[UserRating] = []

    class Config:
        orm_mode = True
