from pydantic import BaseModel

class TokenBase(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: str | None = None


class TokenPayload(BaseModel):
    sub: int | None = None
    exp: int | None = None


class TokenResponse(BaseModel):
    access_token: str