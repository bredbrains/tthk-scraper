from typing import List

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from tthk_scraper.clients.parsers.changes_client import ChangesParserClient
from tthk_scraper.models.change import Change

app = FastAPI()


@app.get('/', status_code=302)
async def redirect_to_school_page():
    return RedirectResponse("https://www.tthk.ee/", status_code=302)


@app.get('/changes', response_model=List[Change], response_model_exclude_none=True)
async def parse_changes():
    return ChangesParserClient().parse()


@app.get('/changes/{date}', response_model=List[Change], response_model_exclude_none=True)
async def parse_changes_by_date(date: str):
    return ChangesParserClient().parse_by_date(date)