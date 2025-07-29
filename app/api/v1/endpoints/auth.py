from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import UserCreate, UserResponse
from database import UserRepository
from api import AuthDep


router = APIRouter()


@router.post('/register', response_model=UserResponse)
async def register(
    user: UserCreate,
    user_repo: UserRepository = Depends(UserRepository)
) -> UserResponse:
    
    return await user_repo.create(user)


@router.post('/login')
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthDep = Depends(AuthDep)
):
    