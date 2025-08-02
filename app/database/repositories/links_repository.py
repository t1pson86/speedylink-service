from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from ..base_repository import BaseRepository
from schemas import LinkCreate
from database import get_new_async_session
from services import LinksRequests




class LinkRepository(BaseRepository[LinkCreate]):

    def __init__(self, session: AsyncSession = Depends(get_new_async_session)):
        super().__init__(session)
        self.links_requests = LinksRequests(
            session = self.session
        )

    
    async def create(
        self,
        link: LinkCreate,
        user_id: int
    ):
        return await self.links_requests.add_link(
            link=link,
            user_id=user_id
            )
        
        
    async def read(
        self
    ):
        return 'ok'
        

    async def update(self, link):
        return 'ok'
    
    
    async def delete(self, id):
        return 'ok'
    
