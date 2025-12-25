import oracledb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#드라이버가 sid인지 service_name인지 헷갈리지 않게 dsn을 명시적으로 만든다.
dsn = oracledb.makedsn(
    host="localhost",
    port=1521,
    sid="ORCL"
)

#DATABASE_URL = "mysql+pymysql://cjg:1234@localhost:3306/home"
DATABASE_URL = f"oracle+oracledb://C##CJG:C##CJG@{dsn}"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db   #이거 모르겠음.
    finally:
        db.close()