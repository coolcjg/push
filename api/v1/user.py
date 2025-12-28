from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from code.ResultCode import ResultCode
from core.database import get_db
from schemas.ApiResponse import ApiResponse
from schemas.getUserListDto import getUserListDto
from crud import user as user_crud
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




