from typing import List

from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse

from tthk_scraper.clients.changes_client import ChangesClient
from tthk_scraper.database import init_db, get_session
from tthk_scraper.models.change import Change

app = FastAPI()


@app.on_event('startup')
def on_startup():
    init_db()


@app.get('/', status_code=302)
async def redirect_to_school_page():
    return RedirectResponse("https://www.tthk.ee/", status_code=302)


@app.get('/changes', response_model=List[Change], response_model_exclude_none=True)
async def parse_changes():
    return ChangesClient().get_changes()


@app.get('/changes/{date}', response_model=List[Change], response_model_exclude_none=True)
async def parse_changes_by_date(date: str):
    return ChangesClient().get_changes_by_date(date)
