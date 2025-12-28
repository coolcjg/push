from sqlalchemy.orm import Session

from common.AES256 import AES256
from models.user import User
from schemas.UserDto import UserDto


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