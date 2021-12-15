from fastapi import FastAPI

from tthk_scraper.database import init_db
from tthk_scraper.views import changes
from tthk_scraper.views import main

app = FastAPI()


@app.on_event('startup')
def on_startup():
    init_db()


app.include_router(main.router)
app.include_router(changes.router)
