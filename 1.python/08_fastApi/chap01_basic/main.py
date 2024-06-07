# fastAPI
# 파이썬으로 작성된 API를 만들기 위한 웹 프레임워크
# 장점
# 1. 고성능
# - 아주 빠른 성능을 제공하며, 기존의 flask 같은 웹 프레임워크 보다 2배 가량 빠르다
# 2. 쉬운 사용
# - 작성하기 쉬운 코드 방식을 가지고 있다.
# 3. 자동 문서화
# - swagger 문서 지원
# 4. 비동기 지원
# - 비동기 기능을 지원하여 비동기 작업을 쉽게 처리할 수 있다.

# uvicorn main:app --reload
# main = main.py 파일
# app = FastAPI 객체
# --reload = 파일 저장 시 서버 재시작

from fastapi import FastAPI
import uvicorn

# fastAPI 생성 및 설정
app = FastAPI()

@app.get("/")
def read_root():
    return { "hello": "world" }


# __name__ : 현재 모듈의 이름을 가지고 있는 내장 변수 (직접 실행된 경우 '__main__'을, import 된 경우 모듈의 파일 명을 가짐)
# main 외 다른 경로에서 서버를 import 하더라도 띄우지 않게 함
# 다만 `uvicorn main:app --reload` 커맨드를 이용하여 실행하는 경우 import 되어 실행되기 때문에 __name__의 값이 'main'이 됨
# `python main.py` 커맨드를 이용하는 경우에만 __name__ = '__main__'이 됨 
if __name__ == '__main__':
    print(__name__)
    uvicorn.run('main:app', reload = True)
