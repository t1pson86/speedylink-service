from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from typing import Optional
from fastapi import HTTPException

from .configuration import jwt_settings
from schemas import TokenPayload


class JWT_verification():

    def __init__(self):
        self.pwd_context = CryptContext(
            schemes = ["bcrypt"],
            deprecated = "auto"
        )


    def get_hash_psw(
        self,
        password: str
    ) -> str:
        
        return self.pwd_context.hash(password)
    

    def get_verify_psw(
        self, 
        plain_password: str, 
        hashed_password: str
    ) -> bool:

        if not self.pwd_context.verify(
            plain_password,
            hashed_password
            ):

            raise HTTPException(
                status_code=400,
                detail="Incorrect email or password"
            )

        return True



    def create_access_token(
        self,
        data: dict,
        expires_delta: Optional[timedelta] = None
    ) -> str:
        
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))

        to_encode.update(
            {"exp": expire}
        )

        return jwt.encode(
            to_encode,
            jwt_settings.JWT_SECRET_KEY,
            algorithm = jwt_settings.JWT_ALGORITHM
        )


    def create_refresh_token(
        self,
        data: dict,
        expires_delta: Optional[timedelta] = None
    ) -> str:
        
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(days=jwt_settings.REFRESH_TOKEN_EXPIRE_DAYS))

        to_encode.update(
            {"exp": expire, "type": "refresh"}
        )

        return jwt.encode(
            to_encode,
            key=jwt_settings.JWT_SECRET_KEY,
            algorithm = jwt_settings.JWT_ALGORITHM
        )
    

    def decode_token(
        self,
        token: str
    ) -> TokenPayload:
        
        try:
            payload = jwt.decode(
                token=token,
                key=jwt_settings.JWT_SECRET_KEY,
                algorithms=[jwt_settings.JWT_ALGORITHM]
            )

            return TokenPayload(**payload)
        except JWTError as e:
            raise e


jwt_ver = JWT_verification()