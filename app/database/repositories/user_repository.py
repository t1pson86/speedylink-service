from sqlalchemy.ext.asyncio import AsyncSession

from ..base_repository import BaseRepository
from schemas import UserCreate
from services import UsersRequests
from database import get_new_async_session
from fastapi import Depends



class UserRepository(BaseRepository[UserCreate]):
    
    def __init__(self, session: AsyncSession = Depends(get_new_async_session)):
        super().__init__(session)
        self.user_requests = UsersRequests(
            session=self.session
        )


    async def create(
        self, 
        user: UserCreate
    ):
        
        return await self.user_requests.add_user(user=user)
        
    async def read(
        self, 
        id: int
    ):
        return await self.user_requests.get_user(id=id)
        
    async def update(self, user):
        return 'ok'
    
    async def delete(self, id):
        return 'ok'

        