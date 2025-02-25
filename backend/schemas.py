import datetime
from typing import List, Optional
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    description: str = None
    content: str = None

    class Config:
        orm_mode = True


class Tags(BaseModel):
    id: int
    tag: List[str]


class User(BaseModel):
    id: int
    email: str
    name: str
    disabled: bool
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None
