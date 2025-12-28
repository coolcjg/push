from pydantic import BaseModel

from schemas.UserDto import UserDto

class getUserListDto(BaseModel):
    pageNum: int
    pageSize:int
    totalCount:int
    users:list[UserDto]