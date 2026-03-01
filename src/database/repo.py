from src.database.models import ShortUrl

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.exceptions import SlugAlreadyExistsError


async def add_slug_to_database(
        slug: str,
        long_url: str,
        session: AsyncSession,
):
    new_slug = ShortUrl(
        slug=slug,
        long_url=long_url,
    )
    session.add(new_slug)
    try:
        await session.commit()
    except IntegrityError:
        raise SlugAlreadyExistsError


async def get_long_url_by_slug_from_database(slug: str, session: AsyncSession) -> str | None:
    query = select(ShortUrl).filter_by(slug=slug)
    result = await session.execute(query)
    res: ShortUrl | None = result.scalar_one_or_none()
    return res.long_url if res.long_url else None
