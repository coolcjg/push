from typing import Optional

from pydantic import BaseModel

class UserDto(BaseModel):

    model_config = {
        "from_attributes": True, # V1의 orm_mode = True와 동일
        "exclude_none": True
    }

    userId:str
    auth:str
    email:Optional[str] = None
    image:Optional[str] = None
    name:str
    socialId:Optional[str] = None
    socialType:Optional[str] = None



