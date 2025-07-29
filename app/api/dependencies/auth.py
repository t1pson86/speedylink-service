from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError
from database import UserRepository, get_new_async_session
from sqlalchemy.ext.asyncio import AsyncSession

from core import jwt_ver


oauth_schem2 = OAuth2PasswordBearer(
            tokenUrl='/api/v1/auth/login',
            scheme_name='JWT'
        )

class AuthDep:

    def __init__(self, session: AsyncSession = Depends(get_new_async_session)):
        self.user_repo = UserRepository(
            session=session
            )

    async def get_current_user(
        self, 
        token: str = Depends(oauth_schem2)
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt_ver.decode_token(
                token=token
            )

            if payload.sub is None:
                raise credentials_exception
            
            current_user = self.user_repo.read(
                id = int(payload.sub)
            )

            return current_user

        except JWTError:
            raise 
        



