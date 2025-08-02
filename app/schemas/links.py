from pydantic import BaseModel, HttpUrl
from typing import Optional

from .users import UserResponse


class LinkCreate(BaseModel):
    long_url: HttpUrl


class LinkResponse(BaseModel):
    id: int
    long_url: str
    short_url: Optional[str] = None

    user: UserResponse