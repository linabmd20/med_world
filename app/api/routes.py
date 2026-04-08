from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.services.user_service import fetch_users_with_accounts

router = APIRouter()


@router.get("/")
def root():
    return {"message": "API running"}


@router.get("/xyz")
def get_xyz():
    if not settings.DB_PASSWORD:
        raise HTTPException(
            status_code=500,
            detail="Missing DB_PASSWORD in environment.",
        )

    try:
        return fetch_users_with_accounts()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Database error: {exc}") from exc
