from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def get_test(
        db: Session = Depends(get_db)
):

    return ""
