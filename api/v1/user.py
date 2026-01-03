from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from code.ResultCode import ResultCode
from core.database import get_db
from dependency.storage import get_storage_service
from schemas.ApiResponse import ApiResponse
from schemas.UserDto import UserDto
from schemas.getUserListDto import getUserListDto
from schemas.user.UserDeleteRequest import UserDeleteRequest
from schemas.user.UserUpdateRequest import UserUpdateRequest
from service import user_service as user_crud
from schemas.user.UserCreateRequest import UserCreateRequest
from service.storage_service import StorageService

user_router = APIRouter()

@user_router.get("/user/list", response_model=ApiResponse[getUserListDto] )
def getUserList(db:Session = Depends(get_db), pageNum:int = Query(1, ge=1), pageSize:int = Query(10, ge=1, le=100)):

    users, user_count = user_crud.get_user_list(db, pageNum, pageSize);

    data = {
        "pageNum": pageNum,
        "pageSize": pageSize,
        "totalCount": user_count,
        "users":users
    }

    return ApiResponse.of(ResultCode.SUCCESS, data)

@user_router.get("/user/{userId}/exists", response_model=ApiResponse[bool])
def get_user_exists(userId:str, db:Session = Depends(get_db)):
    return ApiResponse.of(ResultCode.SUCCESS, user_crud.get_user_exists(db, userId))



@user_router.post("/user", response_model=ApiResponse[UserDto], response_model_exclude_none=True)
def create_user(db:Session = Depends(get_db)
                , request:UserCreateRequest = Depends(UserCreateRequest.as_form)
                , storage_service:StorageService = Depends(get_storage_service)
                ):
    return ApiResponse.of(ResultCode.SUCCESS, user_crud.createUser(db, request, storage_service))


@user_router.get("/user/{userId}", response_model=ApiResponse[UserDto], response_model_exclude_none=True)
def get_user(userId:str, db:Session = Depends(get_db)):
    return ApiResponse.of(ResultCode.SUCCESS, user_crud.get_user(db, userId))


@user_router.put("/user/{userId}", response_model=ApiResponse[UserDto], response_model_exclude_none=True)
def update_user(userId:str, db:Session = Depends(get_db)
                , req:UserUpdateRequest = Depends(UserUpdateRequest.as_form)):
    req.userId = userId
    return ApiResponse.of(ResultCode.SUCCESS, user_crud.update_user(db, req))

@user_router.delete("/users", response_model=ApiResponse[int], response_model_exclude_none=True)
def delete_user(req:UserDeleteRequest, db:Session = Depends(get_db)):
    result = user_crud.delete_users(db, req)
    code = ResultCode.SUCCESS if result > 0 else ResultCode.NOT_EXISTS
    return ApiResponse.of(code, result)

