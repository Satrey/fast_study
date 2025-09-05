import uvicorn
from fastapi import FastAPI

from apps.auth import apps_router

app = FastAPI()

app.include_router(router=apps_router)


def start():
    uvicorn.run(app="lkeep.main:app", reload=True)
