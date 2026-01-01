from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from code.ResultCode import ResultCode
from core.database import get_db
from dependency.storage import get_storage_service
from schemas.ApiResponse import ApiResponse
from schemas.UserDto import UserDto
from schemas.getUserListDto import getUserListDto
from service import user_service as user_crud
from schemas.user.UserCreateRequest import UserCreateRequest
from service.storage_service import StorageService

user_router = APIRouter()

@user_router.get("/user/list", response_model=ApiResponse[getUserListDto] )
def getUserList(db:Session = Depends(get_db), pageNum:int = Query(1, ge=1), pageSize:int = Query(10, ge=1, le=100)):

    users, user_count = user_crud.get_user_list(db, pageNum, pageSize);

    return {
        "code": ResultCode.SUCCESS,
        "message": "ok",
        "data": {
            "pageNum": pageNum,
            "pageSize": pageSize,
            "totalCount": user_count,
            "users":users
        }
    }

@user_router.post("/user", response_model=ApiResponse[UserDto])
def create_user(db:Session = Depends(get_db)
                , request:UserCreateRequest = Depends(UserCreateRequest.as_form)
                , storage_service:StorageService = Depends(get_storage_service)
                ):

    userDto = user_crud.createUser(db, request, storage_service)

    return{
        "code": ResultCode.SUCCESS,
        "message": "ok",
        "data": userDto
    }

@user_router.get("/user/{userId}", response_model=ApiResponse[UserDto], response_model_exclude_none=True)
def get_user(userId:str, db:Session = Depends(get_db)):
    userDto = user_crud.get_user(db, userId)

    return{
        "code": ResultCode.SUCCESS,
        "message": "ok",
        "data": userDto
    }






