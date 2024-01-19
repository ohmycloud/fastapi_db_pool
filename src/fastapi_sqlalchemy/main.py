from fastapi import FastAPI
from routers.user import view as userview
from connection_pool import database_instance
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await database_instance.connect()

# Fast API
app = FastAPI(lifespan=lifespan)

origins = ["*"]
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Including routers
app.include_router(userview.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=3333, reload=True)