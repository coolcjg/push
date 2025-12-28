from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from api.v1.post import router as post_router
from api.v1.user import user_router
from code.ResultCode import ResultCode
from exception.CustomException import CustomException
from schemas.ApiResponse import ApiResponse

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


@app.exception_handler(CustomException)
async def custom_exception_handler(
        request: Request,
        exc: CustomException
):
    return JSONResponse(
        status_code = 200,
        content=ApiResponse(
            code = exc.code,
            message = exc.message,
            data=None
        ).model_dump()
    )


@app.exception_handler(Exception)
async def exception_handler(
        request: Request,
        exc: RuntimeError
):
    return JSONResponse(
        status_code = 500,
        content=ApiResponse(
            code=ResultCode.INTERNAL_ERROR,
            message="Internal server error",
            data=None
        ).model_dump()
    )