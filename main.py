import string
from secrets import choice

from fastapi import FastAPI

app = FastAPI()

ALPHABET = string.ascii_letters + string.digits

@app.post("/short_url")
async def generate_short_url():
    return ...

@app.get("/{slug}")
async def redirect_to_url(slug: str):
    return ...

