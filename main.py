from fastapi import FastAPI

from api.v1.post import router as post_router
from api.v1.user import user_router

#database 테이블 자동 생성
#Base.metadata.create_all(bind=engine)
app = FastAPI(title="Post API")

app.include_router(
    post_router,
    prefix="/api/v1",
    tags=["Post"]
)

app.include_router(
    user_router,
    prefix="/api/v1",
    tags=["User"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
