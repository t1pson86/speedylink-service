from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from schemas import TokenBase

from schemas import UserCreate, UserResponse
from database import UserRepository
from api.dependencies import AuthService

router = APIRouter()


@router.post('/register', response_model=UserResponse)
async def register(
    user: UserCreate,
    user_repo: UserRepository = Depends(UserRepository)
) -> UserResponse:
    
    return await user_repo.create(user)


@router.post('/login', response_model=TokenBase)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends()
):
    
    user = await auth_service.authenticate_user(
        email=form_data.username,
        password=form_data.password
    )

    data_token = await auth_service.create_tokens(user_id=user.id)

    return data_token