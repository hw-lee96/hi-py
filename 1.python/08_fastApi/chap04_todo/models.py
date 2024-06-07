from database import Base, engine, get_db, Session
from sqlalchemy import Column, Integer, Boolean, Text

class DB():
    def db_init():
        # DB 테이블 생성
        Base.metadata.create_all(bind=engine)

    def all_tables():
        return Base.metadata.tables.keys()
    
    get_db = get_db
    Session = Session

    class Todo(Base):
        # 테이블 이름
        __tablename__ = 'todos'

        # 컬럼
        id = Column(Integer, primary_key=True)
        task = Column(Text)
        completed = Column(Boolean, default=False)