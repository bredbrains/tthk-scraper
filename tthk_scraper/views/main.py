from fastapi import APIRouter
from starlette import status
from starlette.responses import RedirectResponse

router = APIRouter()


@router.get("/", status_code=status.HTTP_308_PERMANENT_REDIRECT)
async def redirect_to_school_page():
    return RedirectResponse("https://www.tthk.ee/",
                            status_code=status.HTTP_308_PERMANENT_REDIRECT)
