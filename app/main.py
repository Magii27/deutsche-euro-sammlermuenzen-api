import uvicorn

from fastapi import FastAPI

from app.api import api_v1_router

app = FastAPI(
    title="Deutsche EURO Sammlermuenzen API",
    description="Die API für Deutsche EURO Sammlermünzen",
    version="1.0.0",
    contact={
        "name": "Maksim Hermann",
        "email": "info@software-mh.de"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(api_v1_router, prefix="/api", tags=["API"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
