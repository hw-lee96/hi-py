# 파이썬 내장 DB 라이브러리
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# DB 파일 경로를 지정한 것으로, `todo.sqlite3`이라는 파일 생성 후 사용
DB_URL = 'sqlite:///todo.sqlite3'

# DB 엔진
engine = create_engine(DB_URL)

# DB 세션 연결을 위한 객체
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    db = session_local()
    try:
        yield db # DB 세션 객체 반환
    finally:
        db.close()

# db_session = scoped_session(session_local) # ?

#모든 모델 클래스가 상속받을 기본 모델
Base = declarative_base()