from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


from core import db_settings

class DbSession:

    def __init__(self):
        self.engin = create_async_engine(
            url = f"postgresql+asyncpg://{db_settings.DB_USER}:{db_settings.DB_PASSWORD}@{db_settings.DB_HOST}:{db_settings.DP_PORT}/{db_settings.DB_NAME}",
            echo = False
        )
        self.async_session = async_sessionmaker(
            bind = self.engin,
            class_ = AsyncSession,
            expire_on_commit = False
        )

new_async_session = DbSession()