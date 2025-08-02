
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete

from database import LinksModel
from schemas import LinkCreate



class LinksRequests:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_link(
        self,
        link: LinkCreate,
        user_id: int
    ) -> LinksModel:

        new_link = LinksModel(
            long_url=str(link.long_url),
            user_id=user_id
        )

        self.session.add(new_link)
        await self.session.commit()

        return new_link