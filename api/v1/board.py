from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from crud import board as board_crud
from schemas.board import BoardCreate, BoardResponse

router = APIRouter()


@router.get("/board/list", response_model=list[BoardResponse])
def board_list(db:Session = Depends(get_db)):
    return board_crud.get_board_list(db)

@router.post("/board", response_model=BoardResponse)
def board_create(board: BoardCreate, db:Session = Depends(get_db)):
    return board_crud.create_board(db, board)

@router.get("/board/{board_id}", response_model=BoardResponse)
def board_detail(board_id:int, db:Session = Depends(get_db)):
    board = board_crud.get_board(db, board_id)
    if not board:
        raise HTTPException(status_code=404, detail="게시글 없음")
    return board

@router.put("/board/{board_id}", response_model=BoardResponse)
def board_update(board_id:int, board:BoardCreate, db:Session = Depends(get_db)):
    updated = board_crud.update_board(db, board_id, board)
    if not updated:
        raise HTTPException(status_code=404, detail="수정 대상 없음")
    return updated

@router.delete("/board/{board_id}")
def board_delete(board_id:int, db:Session = Depends(get_db)):
    success = board_crud.delete_board(db,board_id)
    if not success:
        raise HTTPException(status_code=404, detail = "삭제 대상 없음")
    return {"result", "ok"}