from contextlib import asynccontextmanager
from typing import Annotated, AsyncGenerator

from fastapi import Body, FastAPI, status, HTTPException, Depends
from fastapi.responses import RedirectResponse

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import engine, new_session
from src.database.models import Base


from src.exceptions import NoLongUrlFoundError, SlugAlreadyExistsError
from src.service import generate_short_url, get_url_by_slug


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/short_url")
async def generate_short_url(
        long_url: str = Body(embed=True)
):
    return ...

@app.get("/{slug}")
async def redirect_to_url(slug: str):
    return ...

