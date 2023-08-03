from fastapi import FastAPI
from routers import choices

app = FastAPI()

app.include_router(choices.router)