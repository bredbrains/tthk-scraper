from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "mysql+pymysql://root:mysql@localhost:3306/tthk_scraper"

engine = create_engine(
    DATABASE_URL
)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        return session
