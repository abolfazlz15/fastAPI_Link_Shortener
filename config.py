from fastapi import FastAPI

from routers import links

app = FastAPI()

app.include_router(links.router)