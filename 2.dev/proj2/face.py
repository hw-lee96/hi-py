# InsightFace 라이브러리를 이용한 얼굴 탐지 예제

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
## 예시 이미지 불러오기
img1 = cv2.imread('test1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('test4.jpg', cv2.IMREAD_COLOR)

# step4. 추론
faces1 = app.get(img1)
faces2 = app.get(img2)

# step5. 후처리
feats = []
faces1 = np.array(faces1[0].normed_embedding, dtype=np.float32)
faces2 = np.array(faces2[0].normed_embedding, dtype=np.float32)

## 두 이미지의 유사성을 추론 후 -1 ~ 1 사이의 결과 값으로 반환
feats = np.array(feats, dtype=np.float32)
sims = np.dot(faces1, faces2.T)
print(sims)