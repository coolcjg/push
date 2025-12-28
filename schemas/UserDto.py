from typing import Optional

from pydantic import BaseModel

class UserDto(BaseModel):
    userId:str
    auth:str
    email:Optional[str] = None
    image:Optional[str] = None
    name:str
    socialId:Optional[str] = None
    socialType:Optional[str] = None



