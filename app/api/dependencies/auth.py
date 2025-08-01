from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from schemas import TokenBase

from database import UserRepository, get_new_async_session
from core import jwt_settings, jwt_ver
from .cookie import CookieDep



class AuthService:

    def __init__(self, response: Response, session: AsyncSession = Depends(get_new_async_session)):
        self.session = session
        self.cookie_dep = CookieDep(
            response=response
        )
        self.user_repo = UserRepository(
            session=session
        )


    async def authenticate_user(
        self, 
        email: str, 
        password: str
    ):
        try:
            user = await self.user_repo.get_user_by_email(
                email=email
                )

            password_verify = jwt_ver.get_verify_psw(
                password,
                user.hashed_password
            )
            if not user.is_active:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="Inactive user"
                )

            return user
        
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
    
    
    async def create_tokens(
        self,
        user_id: int
    ):
        
        access_token_expires = timedelta(
            minutes=jwt_settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        
        access_token = jwt_ver.create_access_token(
            data={"sub": str(user_id)},
            expires_delta=access_token_expires
        )
        
        refresh_token_expires = timedelta(
            minutes=jwt_settings.REFRESH_TOKEN_EXPIRE_DAYS
            )
        
        refresh_token = jwt_ver.create_refresh_token(
            data={"sub": str(user_id)},
            expires_delta=refresh_token_expires
        )

        self.cookie_dep.set_access_token_cookie(access_token)
        self.cookie_dep.set_refresh_token_cookie(refresh_token)

        return TokenBase(
            access_token=access_token,
            token_type='bearer',
            refresh_token=refresh_token
        )






