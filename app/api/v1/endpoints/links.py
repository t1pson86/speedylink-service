from fastapi import APIRouter, Depends
from api.dependencies import get_current_user

router = APIRouter()

@router.get('')
async def links(url_: str, token: str = Depends(get_current_user)):
    return url_ + '77777'