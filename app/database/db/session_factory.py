from .db import new_async_session


async def get_new_async_session():
    async with new_async_session.async_session() as session:
        yield session


