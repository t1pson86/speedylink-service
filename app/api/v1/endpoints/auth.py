from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import UserCreate, UserResponse
from database import UserRepository
from services import AuthService

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
    auth_service: AuthService = Depends(AuthService)
):
    
    user = await auth_service.authenticate_user(
        email=form_data.username,
        password=form_data.password
    )

    return await auth_service.create_tokens(user_id=user.id)