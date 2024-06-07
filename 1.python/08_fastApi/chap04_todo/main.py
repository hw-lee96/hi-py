import uvicorn
from models import DB
from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import os
path = os.path.dirname(os.path.realpath(__file__))

app = FastAPI()

DB.db_init()

# Jinja2 템플릿 엔진 사용
templates = Jinja2Templates(directory=f'{path}/templates')

# 비동기 문법
# Depends() : api호출 시 수행 전 먼저 실행되는 미들웨어의 역할
@app.get('/')
async def home(request: Request, db: DB.Session=Depends(DB.get_db)):
    # DB에서 todo 모델 조회. id 기준 내림차순 정렬
    todos = db.query(DB.Todo).order_by(DB.Todo.id.desc())
    # 인덱스 템플릿을 렌더링하여 반환
    return templates.TemplateResponse('index.html', {'request': request, 'todos': todos})

# Form(...) : form 태그로 넘어온 값
@app.post('/add')
async def add(request: Request, db: DB.Session=Depends(DB.get_db), task: str=Form(...)):
    todo = DB.Todo(task = task) # todo 객체 생성
    db.add(todo) # db insert
    db.commit() # db commit

    # 요청 처리 후 home 경로로 redirect 하도록 반환
    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)

@app.get('/edit/{todo_id}')
async def edit(request: Request, todo_id: int, db: DB.Session=Depends(DB.get_db)):
    if todo_id == None:
        return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)
    else:
        todo = db.query(DB.Todo).filter(DB.Todo.id == todo_id).first() # .one()
        return templates.TemplateResponse('edit.html', {'request': request, 'todo': todo})

@app.post('/edit/{todo_id}')
async def edit(request: Request, todo_id: int, db: DB.Session=Depends(DB.get_db), task: str=Form(...), completed: bool=Form(False)):
    db.query(DB.Todo).filter(DB.Todo.id == todo_id).update({DB.Todo.task: task, DB.Todo.completed: completed}, synchronize_session=False)

    # todo = db.query(DB.Todo).filter(DB.Todo.id == todo_id).first()
    # todo.task = task
    # todo.completed = completed

    db.commit()

    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)

@app.get('/delete/{todo_id}')
async def edit(request: Request, todo_id: int, db: DB.Session=Depends(DB.get_db)):
    db.query(DB.Todo).filter(DB.Todo.id == todo_id).delete(synchronize_session=False)
    db.commit()

    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)

@app.get('/change/{todo_id}')
async def change(request: Request, todo_id: int, db: DB.Session=Depends(DB.get_db)):
    todo = db.query(DB.Todo).filter(DB.Todo.id == todo_id).first()
    todo.completed = False if todo.completed == True else True
    db.commit()

    return RedirectResponse(url=app.url_path_for('home'), status_code=status.HTTP_303_SEE_OTHER)
    
if __name__ == '__main__':
    uvicorn.run('main:app', port = 8001, reload = True)