import secrets
import string
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from database import LinksModel
from schemas import LinkCreate


def secure_random_string(length: int =10):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))


class LinksRequests:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_link(
        self,
        link: LinkCreate,
        user_id: int
    ) -> str:

        result = await self.session.execute(
            select(LinksModel)
            .where(LinksModel.long_url==str(link.long_url))
            )

        current_url = result.scalars().first()

        if current_url:
            return f"http://127.0.0.1:8000/api/v1/links?short_url={current_url.short_url}"

        new_link = LinksModel(
            long_url=str(link.long_url),
            short_url=secure_random_string(),
            user_id=user_id
        )

        self.session.add(new_link)
        await self.session.commit()

        return f"http://127.0.0.1:8000/api/v1/links?short_url={new_link.short_url}"
    


    async def get_redirect_url(
            self,
            short_url: str
    ) -> str:
        
        current_url = await self.session.execute(
            select(LinksModel)
            .where(LinksModel.short_url==short_url)
            )

        result = current_url.scalars().first()

        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='URL NOT FOUND'
                )

        return result.long_url