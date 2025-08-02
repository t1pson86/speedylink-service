from fastapi import Response, Request, HTTPException, status

from schemas import TokenBase 


class CookieDep():

    def __init__(self, response: Response, request: Request):
        self.response = response
        self.request = request
    def set_access_token_cookie(self, access_token: str):
        if self.request.cookies.get("access_token"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='The user is already authenticated'
            )
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
        if self.request.cookies.get("refresh_token"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='The user is already authenticated'
            )
        
        self.response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,     
            secure=True,         
            samesite="lax"
        )
        return True
    
    
    
    def delete_tokens(self):
        self.response.delete_cookie(
            "access_token"
        )
        self.response.delete_cookie(
            "refresh_token"
        )

        return True


