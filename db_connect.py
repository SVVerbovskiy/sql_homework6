from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:
    DSN = "postgresql://postgres:7753191@localhost:5432/homework6"
    engine = create_engine(DSN)

    Session = sessionmaker(bind=engine)()
