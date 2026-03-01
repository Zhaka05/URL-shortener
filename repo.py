from database.db import new_session
from database.models import ShortUrl

async def add_slug_to_database(slug: str, long_url: str):
    async with new_session() as session:
        new_slug = ShortUrl(slug=slug, long_url=long_url)
        session.add(new_slug)
