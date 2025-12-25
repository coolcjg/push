from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class PostBase(BaseModel):
    title:str
    content:str
    user_id:str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    post_id: int
    reg_date: datetime
    mod_date: Optional[datetime]

    class Config:
        from_attributes = True