import uvicorn
import asyncio

from fastapi import FastAPI

from api import router
from database import new_async_session, Base


app = FastAPI()

app.include_router(
    router=router
    )

async def create_db():
    async with new_async_session.engin.begin() as conn:
        await conn.run_sync(
            Base.metadata.drop_all
        )
        await conn.run_sync(
            Base.metadata.create_all
        ) 


async def main():
    await create_db()


if __name__ == '__main__':
    try:
        asyncio.run(main())
        uvicorn.run(
            'main:app',
            reload=True
        )
    except Exception as e:
        print(e)