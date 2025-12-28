from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime, CheckConstraint

from core.database import Base

class User(Base):
    __tablename__ = "HOME_USER"

    user_id = Column(
        String(100),
        primary_key=True,
        index=True,
        nullable=False
    )

    auth = Column(
        String(10),
        nullable=False
    )

    email = Column(
        String(200),
        nullable=True
    )

    image = Column(
        String(255),
        nullable=True
    )

    mod_date = Column(
        DateTime,
        nullable=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    reg_date = Column(
        DateTime,
        default=datetime.now(timezone.utc)
    )

    social_id = Column(
        String(255),
        nullable=True
    )

    social_type = Column(
        String(255),
        nullable=True
    )

    __table_args__ = (
        CheckConstraint(
            "SOCIAL_TYPE IN ('GOOGLE', 'KAKAO', 'NAVER')",
            name="CK_HOME_USER_SOCIAL_TYPE"
        ),
    )