from fastapi import FastAPI, Form
import uvicorn

# step 1. import modules (모듈 다운로드)
from transformers import pipeline

# step 2. create inference instance (추론 객체 생성)
classifier = pipeline("sentiment-analysis", model="snunlp/KR-FinBert-SC")

app = FastAPI()


@app.post("/text/")
async def text(text: str = Form()):
    result = classifier(text)
    print(result[0])
    result[0]['label'] = '중립적' if result[0]['label'] == 'neutral' else '부정적' if result[0]['label'] == 'negative' else '긍정적'
    return { "result": result }

if __name__ == '__main__':
    uvicorn.run('5_text_cls_api:app', port = 8001, reload = True)