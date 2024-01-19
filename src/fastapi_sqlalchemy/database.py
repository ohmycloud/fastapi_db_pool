from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import settings

# SQLALCHEMY_DATABASE_URL = f'postgresql://{postgres}:{root}@{127.0.0.1}:{5432}/{postgres}'
print("settings.hostname", settings.hostname)
print("settings.port", settings.port)
print("settings.db_name", settings.db_name)
print("settings.db_username", settings.db_username)
print("settings.db_password", settings.db_password)


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.db_username}:{settings.db_password}@{settings.hostname}:{settings.port}/{settings.db_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
