from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from fastapi import HTTPException
from database import UsersModel
from schemas import UserCreate, UserResponse

from core import jwt_ver



class UsersRequests:

    def __init__(self, session: AsyncSession):
        self.session = session


    async def get_user(
        self, 
        id: int
    ) -> UsersModel:
        
        result = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.id==id)
            )
        user = result.scalars().first()

        if user is None:
            raise HTTPException(
                status_code=401,
                detail='Could not validate credentials'
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
            raise HTTPException(
                status_code=400,
                detail='This email address is already registered'
                )
        
        new_user = UsersModel(
            name=user.name.strip(),
            email=user.email.strip(),
            hashed_password=jwt_ver.get_hash_psw(
                user.hashed_password.strip()
                )
            )

        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user


    async def get_email(
        self, 
        email: str
    ) -> UserResponse | None:
        
        result = await self.session.execute(
            select(UsersModel)
            .where(UsersModel.email==email)
            )
        return result.scalars().first()


