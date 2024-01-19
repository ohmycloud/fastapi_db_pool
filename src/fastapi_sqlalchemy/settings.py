from pydantic_settings import BaseSettings


# This is a pydantic model for the enviroment variables
class Settings(BaseSettings):
    hostname: str
    port: str
    db_name: str
    db_username: str
    db_password: str

    class Config:
        env_file = ".env"


settings = Settings()
