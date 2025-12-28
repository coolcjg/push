from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: str
    auth: str
    email: str
    name: str
    password: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    mod_date:Optional[datetime]
    reg_date:Optional[datetime]
    social_id:Optional[str]
    social_type:Optional[str]



