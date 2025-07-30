from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_new_async_session, UserRepository
from datetime import timedelta


from core import jwt_ver, jwt_settings
from schemas import TokenBase


class AuthService:

    def __init__(self, session: AsyncSession = Depends(get_new_async_session)):
        self.session = session
        self.user_repo = UserRepository(
            session=session
        )


    async def authenticate_user(
        self, 
        email: str, 
        password: str
    ):
        
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

        return TokenBase(
            access_token=access_token,
            token_type='bearer',
            refresh_token=refresh_token
        )


            
            

        



