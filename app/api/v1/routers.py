from fastapi import APIRouter

from .endpoints import auth

router = APIRouter(prefix='/api/v1', tags=['v1'])

router.include_router(router=auth.router, prefix='/users')
