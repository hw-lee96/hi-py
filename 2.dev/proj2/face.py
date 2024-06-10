# docu : https://pypi.org/project/insightface/

# 1. pip install insightface

# 2. example test
# - onnxruntime 관련 에러 : onnxruntime 설치해야 됨
# - onnxruntime docu : https://onnxruntime.ai/getting-started
# - pip install onnxruntime

# step1. 모듈 import
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

# step2. 추론 모델 생성
## CUDAExecutionProvider : GPU로 연산할 때 옵션에 추가
app = FaceAnalysis(providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

# step3. 데이터 가져오기
## insightface 패키지에 포함되어 있는 예시 이미지 불러오기
img = ins_get_image('t1')

# step4. 추론
faces = app.get(img)

# step5. 후처리
rimg = app.draw_on(img, faces)
## 신규 이미지 생성
cv2.imwrite("./t1_output.jpg", rimg)