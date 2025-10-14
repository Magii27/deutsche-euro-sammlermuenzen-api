from fastapi import APIRouter

from app.api.auth.auth_router import auth_router

from app.api.v1.muenze_router import muenze_router
from app.api.v1.serie_router import serie_router
from app.api.v1.praegung_router import praegung_router

api_v1_router = APIRouter(prefix="/v1", tags=["v1"])

api_v1_router.include_router(auth_router)

api_v1_router.include_router(muenze_router)
api_v1_router.include_router(serie_router)
api_v1_router.include_router(praegung_router)
