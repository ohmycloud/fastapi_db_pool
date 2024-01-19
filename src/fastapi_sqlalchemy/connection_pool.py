import asyncpg
from settings import settings


async def get_pool() -> asyncpg.Pool:
    pool = await asyncpg.create_pool(
        min_size=1,
        max_size=10,
        command_timeout=60,
        host=settings.hostname,
        port=settings.port,
        database=settings.db_name,
        user=settings.db_username,
        password=settings.db_password
    )
    if pool is None:
        raise ValueError("Could not create connection pool")
    return pool
