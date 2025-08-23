from fastapi import APIRouter

from app.api.v1.muenze_router import muenze_router

api_v1_router = APIRouter(prefix="/v1", tags=["v1"])

api_v1_router.include_router(muenze_router)
