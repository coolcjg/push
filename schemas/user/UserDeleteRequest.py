from typing import List

from pydantic import BaseModel


class UserDeleteRequest(BaseModel):
    userIds:List[str]

