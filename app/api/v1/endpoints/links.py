from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from api.dependencies import get_current_user

from schemas import LinkCreate, UserBase
from database import LinkRepository

router = APIRouter()

@router.post('', response_class=HTMLResponse)
async def add_new_link(
    link: LinkCreate,
    link_repo: LinkRepository = Depends(),
    token: UserBase = Depends(get_current_user)
):

    return await link_repo.create(
        link=link,
        user_id=token.id
    )
