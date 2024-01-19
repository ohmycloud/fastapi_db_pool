from fastapi import status, HTTPException, APIRouter, Depends
import asyncpg
from .serializer import UserBase
from .models import User
from fastapi_sqlalchemy.connection_pool import get_pool


router = APIRouter(
    prefix="/users",
    tags=['user']
)


# fetch data from postgresql
@router.get("/fetch", status_code=status.HTTP_201_CREATED)
async def get_user(db_pool: asyncpg.Pool = Depends(get_pool)):
    """Handle incoming requests."""
    async with db_pool.acquire() as connection:
        try:
            return await connection.fetch(query="SELECT * FROM public.user")
        except Exception as err:
            print(err.args[0])
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=err.args[0])


# insert data into postgres
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db_pool: asyncpg.Pool = Depends(get_pool)):
    db_user = User(**dict(user))
    query = """INSERT INTO public.user (id, fname, lname, email, password) VALUES 
       ({}, '{}', '{}', '{}', '{}')""".format(db_user.id,
                                              db_user.fname,
                                              db_user.lname,
                                              db_user.email,
                                              db_user.password)
    async with db_pool.acquire() as connection:
        try:
            result = await connection.execute(query=query)

            if result == "INSERT 0 1":
                return db_user
            else:
                print('Something went wrong')

        except Exception as e:
            print(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=e)
