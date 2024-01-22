import asyncpg
from settings import settings
from asyncpg import Pool
from typing import Optional


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
    else:
        print('init a postgres connection pool')

    return pool


class UninitializedDatabasePoolError(Exception):
    def __init__(
        self,
        message="The database connection pool has not been properly initialized.Please ensure setup is called",
    ):
        self.message = message
        super().__init__(self.message)


class DataBasePool:

    _db_pool: Optional[Pool] = None

    @classmethod
    async def setup(cls, timeout: Optional[float] = None):
        cls._db_pool = await asyncpg.create_pool(
            min_size=1,
            max_size=10,
            command_timeout=60,
            host=settings.hostname,
            port=settings.port,
            database=settings.db_name,
            user=settings.db_username,
            password=settings.db_password
        )
        cls._timeout = timeout

    @classmethod
    async def get_pool(cls):
        if not cls._db_pool:
            await cls.setup()

        print('starting get connection pool')
        return cls._db_pool

    @classmethod
    async def teardown(cls):
        if not cls._db_pool:
            await cls.setup()

        print('starting shut done connection pool')
        await cls._db_pool.close()

