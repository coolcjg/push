from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from service import post_service as post_crud
from schemas.post import PostCreate, PostResponse

router = APIRouter()


@router.get("/post/list", response_model=list[PostResponse])
def post_list(db:Session = Depends(get_db)):
    return post_crud.get_post_list(db)

@router.post("/post", response_model=PostResponse)
def post_create(post: PostCreate, db:Session = Depends(get_db)):
    return post_crud.create_post(db, post)

@router.get("/post/{post_id}", response_model=PostResponse)
def post_detail(post_id:int, db:Session = Depends(get_db)):
    post = post_crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="게시글 없음")
    return post

@router.put("/post/{post_id}", response_model=PostResponse)
def post_update(post_id:int, post:PostCreate, db:Session = Depends(get_db)):
    updated = post_crud.update_post(db, post_id, post)
    if not updated:
        raise HTTPException(status_code=404, detail="수정 대상 없음")
    return updated

@router.delete("/post/{post_id}")
def post_delete(post_id:int, db:Session = Depends(get_db)):
    success = post_crud.delete_post(db,post_id)
    if not success:
        raise HTTPException(status_code=404, detail = "삭제 대상 없음")
    return {"result", "ok"}