# Image Classification : 이미지 분류
# 업로드한 이미지 추론 후 분류하여 결과 값을 반환하는 api 개발 / 테스트

# docu : https://fastapi.tiangolo.com/ko/

# mp와 fastapi 연계
# 1. 현재 가상환경에 fastapi, uvicorn install 진행
# - pip install fastapi
# - pip install "uvicorn[standard]"
#
# 2. 예제 테스트
# - 현재는 아래 커맨드가 아닌 파이썬 파일 자체를 실행하는 방식의 예제임 ex) 커맨드 : python cls_api.py
# - uvicorn 서버를 실행하는 커맨드 : uvicorn [파일명]:[서버 변수명]
# - ex) uvicorn cls_api:app

from fastapi import FastAPI, File, UploadFile
import uvicorn
import os
path = os.path.dirname(os.path.realpath(__file__))

# 3. mp 관련 모듈 추가
# 3.1. STEP 1: 필요한 모듈 가져오기
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision

# 3.2. STEP 2: 추론기 생성
# 모델을 서버 실행과 동시에 한 번 만들고 서버가 유지되는 동안 계속 이용이 가능하도록 서버 생성 전 & api 밖에 생성해야 함
base_options = python.BaseOptions(model_asset_path='2.dev\\proj1\\models\\efficientnet_lite0.tflite')
options = vision.ImageClassifierOptions(base_options=base_options, max_results=3) # max_resuts : 반환 받으려는 결과 값의 개수
classifier = vision.ImageClassifier.create_from_options(options)

app = FastAPI()

# File() 함수를 통해 파일을 전달받은 경우 바이트의 형태로 이미 OS에 전달이 되었기 때문에 사이즈 측정이 가능하다
# 다만 한 번에 하나씩만 전달이 됨
@app.post("/files/")
async def create_file(file: bytes = File()): 
    return {"file_size": len(file)}

import io
import PIL
import numpy as np

# UploadFile
# - UploadFile에서는 http head에 담겨져있는 파일의 meta data만 전달됨
# - 실제 파일은 전달되지 않았기 때문에 파일 자체의 내용은 알 수 없음
# - file.read()를 통해 파일의 내용을 읽어와야 사용이 가능
# - 만약 파일의 타입을 체크해야하는 경우 UploadFile을 통해 전부가 아닌 meta data만 전달받아서 체크 후 read 하는 방식이 부하를 줄이고 효율적
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # 추론을 위해 이미지를 읽어옴
    byte_file = await file.read()

    # byte 형식에서 binary로 변환
    image_bin = io.BytesIO(byte_file)
    
    # 디코딩하여 binary 형식에서 파이썬에서 읽을 수 있는 형태인 비트맵 형식으로 변경
    pil_image = PIL.Image(image_bin)

    # 파이썬에서 비트맵을 다루는 표준 자료형인 np.asarray로 한 번 더 변환
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_image))

    # STEP 4: 이미지 추론
    classification_result = classifier.classify(image)

    # STEP 5: 추론 결과 내용 후처리
    # - classifications : 요청한 사진들 자체의 추론 결과를 가지고 있는 배열. 여러장을 요청하는 경우 인덱스로 접근
    top_category = classification_result.classifications[0].categories
    result = []
    for item in top_category:
        result.append({ 'category_name': item.category_name, 'percentage' : f'{item.score * 100:.2f}%' })

    # return {'category_name': top_category.category_name, 'percentage' : f'{top_category.score * 100:.2f}%',"file_size": len(byte_file)}
    return result

if __name__ == '__main__':
    uvicorn.run('cls_api:app', port = 8001, reload = True)

