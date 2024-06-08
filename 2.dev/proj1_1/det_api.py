# Object Detection : 객체 탐지
# 업로드한 이미지 내의 객체를 탐지한 후 결과 값을 반환하는 api 개발 / 테스트

# step 1. fastapi, uvicorn install 관련 내용은 proj1_1/cls_api 참조
from fastapi import FastAPI, File, UploadFile
import uvicorn
import os
path = os.path.dirname(os.path.realpath(__file__))

import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: 추론기 생성
# 모델을 서버 실행과 동시에 한 번 만들고 서버가 유지되는 동안 계속 이용이 가능하도록 서버 생성 전 & api 밖에 생성해야 함
base_options = python.BaseOptions(model_asset_path='2.dev\\proj1\\models\\efficientdet_lite0.tflite')

# score_threshold : 값이 높으면 빡빡하게, 낮으면 널널하게 객체를 찾음. 보통 기본값으로 0.5를 사용
options = vision.ObjectDetectorOptions(base_options=base_options, score_threshold=0.5) 
detector = vision.ObjectDetector.create_from_options(options)

app = FastAPI()

import io
import PIL
import numpy as np

@app.post("/det_image/")
async def create_upload_file(file: UploadFile):
    byte_file = await file.read()
    image_bin = io.BytesIO(byte_file)
    pil_img = PIL.Image.open(image_bin)

    # Convert MP Image from PIL IMAGE
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_img))

    # STEP 4: Classify the input image.
    detection_result = detector.detect(image)

    # STEP 5: Process the classification result. In this case, visualize it.
    # 어떤 객체가 몇 개 존재하는지를 반환하도록 로직 구현
    animals = {}
    for item in detection_result.detections:
        if animals.get(item.categories[0].category_name) == None:
            animals[item.categories[0].category_name] = 1
        else:
            animals[item.categories[0].category_name] += 1

    # 요청된 형태에 맞게 변환
    result = []
    for key in animals.keys():
        result.append({ 'result': { 'category': key, 'count': animals[key] } })
        
    return result 

if __name__ == '__main__':
    uvicorn.run('det_api:app', port = 8001, reload = True)

