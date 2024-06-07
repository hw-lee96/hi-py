from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 경로 매개변수 : URL에 포함되어 전달되는 매개변수
@app.get('/users/1/{user_id}')
def get_user(user_id):
    return { 'user_id' : user_id }

# 타입 정의가 가능
@app.get('/users/2/{user_id}')
def get_user_id(user_id : int):
    return { 'user_id' : user_id }

# 인터프리터 언어이기 때문에 2번과 같이 이미 타입 정의가 된 api가 위에 존재하면 아래의 api는 접근 시 에러 발생
# 이를 해결하기 위해서는 겹치는 api 보다 위에 선언하면 됨
@app.get('/uses/2/a')
def get_current_user():
    return { 'user_id' : 'a' }

# 쿼리 스트링 파라미터
# 호스트주소/path? 뒤에오는 변수들
# & 기호로 구분 되며 key=value 쌍으로 전달
@app.get('/users')
def get_users(limit: int, name: str):
    return { 'limit' : limit, 'name' : name }

# swagger : /docs

# 매개변수 기본 값 지정
@app.get('/users/3')
def get_users_2(limit: int = 10):
    return { 'limit' : limit }

if __name__ == '__main__':
    # uvicorn.run(app:'main:app', port:8001, reload:True) 
    # uvicorn main:app --reload --port:8001
    uvicorn.run('main:app', port = 8001, reload = True)