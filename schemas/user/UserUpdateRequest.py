from typing import Optional

from fastapi import UploadFile, Form, File
from pydantic import BaseModel


class UserUpdateRequest(BaseModel):
    userId:str | None = None
    name:str
    password:str
    auth:str
    image:UploadFile | None = None

    @classmethod
    def as_form(
            cls,
            name:str = Form(...),
            password:str = Form(...),
            auth:str = Form(...),
            image:Optional[UploadFile] = File(None)
    ):
        return cls(
            name=name,
            password=password,
            auth=auth,
            image=image
        )
