from fastapi import APIRouter

from .endpoints import auth, links

router = APIRouter(
    prefix='/api/v1', 
    tags=['v1']
    )

router.include_router(router=auth.router, prefix='/auth')
router.include_router(router=links.router, prefix='/links')
