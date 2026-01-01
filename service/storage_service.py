import os
import uuid

from fastapi import UploadFile


class StorageService:

    def save_image(self, file: UploadFile) -> str:

        print(file.filename)
        ext = os.path.splitext(file.filename)[1]
        print("ext:", ext)
        filename = f"{uuid.uuid4()}{ext}"
        print("filename:", filename)
        path = f"D:/NAS/home_storage/uploads/{filename}"

        with open(path, "wb") as f:
            f.write(file.file.read())

        return path