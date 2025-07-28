from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import UserCreate, UserResponse
from database import UserRepository
# from api.dependencies import user_rst


router = APIRouter()

@router.post('', response_model=UserResponse)
async def add_user(
    user: UserCreate,
    user_repo: UserRepository = Depends(UserRepository)
):
    return await user_repo.create(user)
    
