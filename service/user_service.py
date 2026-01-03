from sqlalchemy.orm import Session

from common.password_encoder import hash_password
from schemas.user.UserDeleteRequest import UserDeleteRequest
from schemas.user.UserUpdateRequest import UserUpdateRequest
from service.storage_service import StorageService
from code.ResultCode import ResultCode
from common.AES256 import AES256
from exception.CustomException import CustomException
from models.user import User
from schemas.UserDto import UserDto
from schemas.user.UserCreateRequest import UserCreateRequest


def get_user_list(db:Session, pageNum:int = 1, pageSize: int = 10):

    offset = (pageNum-1)*pageSize;
    total_count = db.query(User).count();

    users = (
        db.query(User)
        .order_by(User.reg_date.desc())
        .offset(offset)
        .limit(pageSize)
        .all()
    )

    aes = AES256()

    user_dtos=[
        UserDto(
            userId = u.user_id,
            auth   = u.auth,
            email  = u.email,
            image  = u.image,
            name   = aes.decrypt(u.name),
            socialType = u.social_type
        )
        for u in users
    ]

    print("total_count:",total_count)
    print("users", user_dtos)

    return user_dtos, total_count


def createUser(db:Session, request:UserCreateRequest, storageService:StorageService):


    image_path = None
    if request.image:
        image_path = storageService.save_image(request.image)

    exists = (
        db.query(User)
        .filter(User.user_id == request.userId)
        .first()
    )

    if exists:
        raise CustomException(ResultCode.USER_EXISTS)

    aes = AES256()

    user = User(
        user_id = request.userId,
        name = aes.encrypt(request.name),
        password = hash_password(request.password),
        image = image_path,
        auth = request.auth,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    userDto = UserDto(
        userId=user.user_id,
        auth=user.auth,
        name=aes.decrypt(user.name),
        image=user.image
    )

    return userDto


def get_user(db:Session, user_id:str) -> UserDto:
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise CustomException(ResultCode.NOT_EXISTS)

    aes = AES256()
    userDto = UserDto(
        userId=user.user_id,
        auth=user.auth,
        name=aes.decrypt(user.name),
        image=user.image
    )

    return  userDto

def update_user(db:Session, req:UserUpdateRequest):
    user = db.query(User).filter(User.user_id == req.userId).first()
    aes = AES256()

    if not user:
        raise CustomException(ResultCode.NOT_EXISTS)

    if req.password is not None:
        user.password = hash_password(req.password)

    if req.name is not None:
        user.name = aes.encrypt(req.name)

    if req.image is not None:
        user.image=  req.image

    if req.auth is not None:
        user.auth = req.auth

    db.commit()
    db.refresh(user)

    return UserDto(
        userId = user.user_id,
        auth = user.auth,
        name = aes.decrypt(user.name),
        image = user.image
    )

def delete_users(db:Session, req:UserDeleteRequest) -> int:
    users = (
        db.query(User)
        .filter(User.user_id.in_(req.userIds))
        .all()
    )

    if not users:
        return 0

    for user in users:
        db.delete(user)

    return len(users)

def get_user_exists(db:Session, user_id:str) -> bool:
    return db.query(User).filter(User.user_id == user_id).first() is not None



