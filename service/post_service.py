from sqlalchemy.orm import Session

from models.post import Post
from schemas.post import PostCreate


def get_post_list(db:Session):
    return db.query(Post).order_by(Post.post_id.desc()).all()

def get_post(db:Session, post_id:int):
    return db.query(Post).filter(Post.post_id == post_id).first()

def create_post(db:Session, post: PostCreate):
    new_post = Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def update_post(db:Session, post_id:int, post:PostCreate):
    db_post = get_post(db, post_id)
    if not db_post:
        return None

    for key, value in post.dict().items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db:Session, post_id:int):
    db_post = get_post(db, post_id)
    if not db_post:
        return False

    db.delete(db_post)
    db.commit()
    return True
