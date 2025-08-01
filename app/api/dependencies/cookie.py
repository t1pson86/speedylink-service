from fastapi import Response, Request

from schemas import TokenBase 


class CookieDep():

    def __init__(self, response: Response):
        self.response = response

    def set_access_token_cookie(self, access_token: str):
        self.response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,     
            secure=True,         
            samesite="lax",
            max_age=30
        )

        return True


    def set_refresh_token_cookie(self, refresh_token: str):
        self.response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,     
            secure=True,         
            samesite="lax"
        )

        return True


