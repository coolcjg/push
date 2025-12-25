from sqlalchemy.orm import Session

from models.board import Board
from schemas.board import BoardCreate


def get_board_list(db:Session):
    return db.query(Board).order_by(Board.id.desc()).all()

def get_board(db:Session, board_id:int):
    return db.query(Board).filter(Board.id == board_id).first()

def create_board(db:Session, board: BoardCreate):
    new_board = Board(**board.model_dump())
    db.add(new_board)
    db.commit()
    db.refresh(new_board)
    return new_board

def update_board(db:Session, board_id:int, board:BoardCreate):
    db_board = get_board(db, board_id)
    if not db_board:
        return None

    for key, value in board.dict().items():
        setattr(db_board, key, value)

    db.commit()
    db.refresh(db_board)   #이거 무슨뜻이지???
    return db_board

def delete_board(db:Session, board_id:int):
    db_board = get_board(db, board_id)
    if not db_board:
        return False

    db.delete(db_board)
    db.commit()
    return True
