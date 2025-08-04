from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from api.dependencies import get_current_user

from schemas import LinkCreate, UserBase, LinkResponse
from database import LinkRepository

router = APIRouter()

@router.post('')
async def add_new_link(
    link: LinkCreate,
    link_repo: LinkRepository = Depends(),
    token: UserBase = Depends(get_current_user)
) -> str:

    return await link_repo.create(
        link=link,
        user_id=token.id
    )


@router.get('')
async def redirect_url(
    short_url: str,
    link_repo: LinkRepository = Depends()
):

    current_url = await link_repo.read(
        short_url = short_url
    )

    return RedirectResponse(
        url=current_url
    )