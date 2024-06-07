# 요청 / 응답
# POST, PUT, PATCH 등의 메소드를 사용하는 경우 HTTP 본문(body) 사용
# 단순 텍스트나 json을 이용한다.

# pydantic으로 요청 본문 받기
# 데이터 유휴성 검사 및 설정 관리를 위한 라이브러리

import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, HttpUrl

# fastAPI 생성 및 설정
app = FastAPI()

# BaseModel을 상속 받아야 request body로 받은 값을 클래스에 바로 대입이 가능함
class UserInfo(BaseModel):
    name: str
    password: str
    url: Optional[HttpUrl] = None

@app.post('/users')
def create_user(user: UserInfo):
    # post에 전달된 body의 내용을 (BaseModel을 상속받은)UserInfo 클래스에 바로 대입하여 객체를 생성
    return user



if __name__ == '__main__':
    uvicorn.run('main:app', port = 8001, reload = True)