from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from fastapi import HTTPException
from database import UsersModel
from schemas import UserCreate, UserResponse



class UsersRequests:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_user(
        self, 
        id: int
    ):
        result = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.id==id)
            )
        user = result.scalars().first()

        if user is None:
            raise HTTPException(
                status_code=404,
                detail='User not found'
            )

        return user
    
    
    async def add_user(
        self, 
        user: UserCreate
    ) -> UserResponse:
        result = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.email==user.email)
            )
        this_user = result.scalars().first()

        if this_user:
            raise HTTPException(status_code=400, detail='This Email not varify')
        
        new_user = UsersModel(
            **user.model_dump()
        )

        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user


