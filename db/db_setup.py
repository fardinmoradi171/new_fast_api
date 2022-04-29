from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


## address and user and password paql:
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://fardin:moradi@localhost/fardindb"



engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={},future=True
)
SessionLocal = sessionmaker(
    autocommit=False,autoflush=False,bind=engine,future=True
)

Base = declarative_base()


##  this method needed for connection to postgresql:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 