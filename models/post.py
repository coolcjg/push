from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime, Numeric, CHAR, Sequence

from core.database import Base


class Post(Base):
    __tablename__ = "HOME_POST"

    post_id = Column(
        Numeric(19,0),
        Sequence("HOME_POST_SEQ"),
        primary_key=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    content = Column(String(255))

    user_id = Column(String(100))

    view_cnt = Column(Numeric(10, 0), nullable=False, default=0)

    open = Column(CHAR(1))

    reg_date = Column(DateTime, default=datetime.now(timezone.utc))

    mod_date = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))


