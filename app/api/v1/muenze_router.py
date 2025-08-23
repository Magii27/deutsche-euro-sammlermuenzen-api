from fastapi import APIRouter

muenze_router = APIRouter(prefix="/muenze", tags=["muenze"])


@muenze_router.get("/")
async def get_muenzen():
    """
    Retrieve all muenzen.
    """
    return {"message": "List of all muenzen"}
