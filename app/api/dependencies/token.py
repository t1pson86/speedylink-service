from fastapi import HTTPException, Depends, status, Request, Response
from fastapi.security import OAuth2
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError
from datetime import timedelta

from database import UserRepository, get_new_async_session
from core import jwt_ver
from core import jwt_settings
from .cookie import CookieDep


class Oauth2CookieBearer(OAuth2):

    def __call__(self, request: Request, response: Response) -> str | None:
        try:
            access_token = request.cookies.get("access_token")

            if not access_token:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated (no access token in cookies)",
                )
        
            return access_token
        
        except Exception:
            try:
                credentials_exception = HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    )
                refresh_token = request.cookies.get("refresh_token")

                if not refresh_token:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Not authenticated (no access token in cookies)",
                    )
                
                payload = jwt_ver.decode_token(
                    token = refresh_token
                )

                if payload.sub is None:
                    raise credentials_exception
                
                new_access_token = jwt_ver.create_refresh_token(
                    data={"sub": str(payload.sub)},
                    expires_delta=timedelta(minutes=jwt_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
                )

                cookie_dep = CookieDep(
                    response=response
                )

                cookie_dep.set_access_token_cookie(
                    access_token = new_access_token
                )

                return refresh_token


            except Exception:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                )
    

Oauth2Cookie_scheme = Oauth2CookieBearer()



async def get_current_user(
    session: AsyncSession = Depends(get_new_async_session),
    token: str = Depends(Oauth2Cookie_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt_ver.decode_token(
            token
        )

        if payload.sub is None:
            raise credentials_exception
        
        user_repo = UserRepository(
            session=session
        )

        current_user = await user_repo.read(
            id = int(payload.sub)
        )
        return current_user
    
    except JWTError:
        raise credentials_exception
    
