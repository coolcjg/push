from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db   #이거 모르겠음.
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/board/list", response_model=list[schemas.BoardResponse])
def board_list(db:Session = Depends(get_db)):
    return crud.get_board_list(db)

@app.post("/board", response_model=schemas.BoardResponse)
def board_create(board: schemas.BoardCreate, db:Session = Depends(get_db)):
    return crud.create_board(db, board)

@app.get("/board/{board_id}", response_model=schemas.BoardResponse)
def board_detail(board_id:int, db:Session = Depends(get_db)):
    board = crud.get_board(db, board_id)
    if not board:
        raise HTTPException(status_code=404, detail="게시글 없음")
    return board

@app.put("/board/{board_id}", response_model=schemas.BoardResponse)
def board_update(board_id:int, board:schemas.BoardCreate, db:Session = Depends(get_db)):
    updated = crud.update_board(db, board_id, board)
    if not updated:
        raise HTTPException(status_code=404, detail="수정 대상 없음")
    return updated

@app.delete("/board/{board_id}")
def board_delete(board_id:int, db:Session = Depends(get_db)):
    success = crud.delete_board(db,board_id)
    if not success:
        raise HTTPException(status_code=404, detail = "삭제 대상 없음")
    return {"result", "ok"}