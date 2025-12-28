from typing import TypeVar, Generic

from pydantic import BaseModel

T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    code:str
    message:str
    data:T