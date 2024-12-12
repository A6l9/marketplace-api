from api.initial import api_router, app
from database.initial import db
from contextlib import asynccontextmanager
from utils.price_convertor import main
from fastapi import FastAPI
from loguru import logger
import fcntl
import asyncio


@asynccontextmanager
async def lifespan(app: FastAPI):
    with open('.lock', 'w') as lock_file:
        try:
            fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
            await db.initial()
            asyncio.create_task(main())
            yield
        except BlockingIOError:
            logger.info('The task is already running in another process')
            yield


root_app = FastAPI(lifespan=lifespan)
root_app.mount('/api/v1', app)
app.include_router(api_router, tags=['Routes'])
