from typing import TypeVar, Generic

from pydantic import BaseModel

from code.ResultCode import ResultCode

T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    code:str
    message:str
    data:T | None = None

    @classmethod
    def of(cls, result_code: ResultCode, data=None) -> ApiResponse[T]:
        return cls(code=result_code, message=result_code.message, data=data)