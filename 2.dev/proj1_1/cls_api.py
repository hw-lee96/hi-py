# Image Classification : 이미지 분류
# 업로드한 이미지 추론 후 분류하여 결과 값을 반환하는 api 개발 / 테스트

# STEP 1: 필요한 모듈 가져오기
from fastapi import FastAPI, File, UploadFile
import uvicorn
import os
path = os.path.dirname(os.path.realpath(__file__))

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision

# STEP 2: 추론기 생성
base_options = python.BaseOptions(model_asset_path='2.dev\\proj1\\models\\efficientnet_lite0.tflite')
options = vision.ImageClassifierOptions(base_options=base_options, max_results=3) # max_resuts : 반환 받으려는 결과 값의 개수
classifier = vision.ImageClassifier.create_from_options(options)

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File()): 
    return {"file_size": len(file)}

import io
import PIL
import numpy as np

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    byte_file = await file.read()

    # STEP 3: Load the input image.
    #image = mp.Image.create_from_file(IMAGE_FILENAMES[1])

    # convert char array to binary array
    image_bin = io.BytesIO(byte_file)
    
    # create PIL Image from binary array
    pil_img = PIL.Image.open(image_bin)

    # Convert MP Image from PIL IMAGE
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_img))

    # STEP 4: Classify the input image.
    classification_result = classifier.classify(image)

    # STEP 5: Process the classification result. In this case, visualize it.
    top_category = classification_result.classifications[0].categories[0]
    return {'category_name': top_category.category_name, 'percentage' : f'{top_category.score * 100:.2f}%',"file_size": len(byte_file)}

if __name__ == '__main__':
    uvicorn.run('cls_api:app', port = 8001, reload = True)

