from fastapi import FastAPI

from core.database import engine, Base
from  api.v1.board import router as board_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Board API")

app.include_router(
    board_router,
    prefix="/api/v1",
    tags=["Board"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
