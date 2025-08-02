from fastapi import APIRouter, Depends
from api.dependencies import get_current_user

from schemas import LinkCreate, UserBase, LinkResponse
from database import LinkRepository

router = APIRouter()

@router.post('', response_model=LinkResponse)
async def add_new_link(
    link: LinkCreate,
    link_repo: LinkRepository = Depends(),
    token: UserBase = Depends(get_current_user)
):

    return await link_repo.create(
        link=link,
        user_id=token.id
    )
