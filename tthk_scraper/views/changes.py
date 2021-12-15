from typing import List

from fastapi import APIRouter

from tthk_scraper.clients.changes_client import ChangesClient
from tthk_scraper.models.change import Change

router = APIRouter(prefix="/changes")


@router.get('/', response_model=List[Change], response_model_exclude_none=True)
async def parse_changes():
    return ChangesClient().get()


@router.get('/{date}', response_model=List[Change], response_model_exclude_none=True)
async def parse_changes_by_date(date: str):
    return ChangesClient().get_by_date(date)
