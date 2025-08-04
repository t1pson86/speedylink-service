import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


# -- DATABASE SETTINGS -- 
class DbSettings(BaseSettings):

    DB_USER: str = os.getenv('DB_USER')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
    DB_HOST: str = os.getenv('DB_HOST')
    DP_PORT: int = os.getenv('DB_PORT')
    DB_NAME: str = os.getenv('DB_NAME')

    class Config:
        env_file = '.env'


db_settings = DbSettings()



# -- JWT SETTINGS --
class JWTSettings(BaseSettings):

    JWT_SECRET_KEY: str = os.getenv('SCR_KEY')
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    
    class Config:
        env_file = ".env"


jwt_settings = JWTSettings()