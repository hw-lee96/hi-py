from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import uvicorn
import os
path = os.path.dirname(os.path.realpath(__file__))

# 3. mp 관련 모듈 추가
# 3.1. STEP 1: 필요한 모듈 가져오기
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# 3.2. STEP 2: 추론기 생성
# 모델을 서버 실행과 동시에 한 번 만들고 서버가 유지되는 동안 계속 이용이 가능하도록 서버 생성 전 & api 밖에 생성해야 함
base_options = python.BaseOptions(model_asset_path='2.dev\\proj1\\models\\efficientdet_lite0.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options, score_threshold=0.5) # score_threshold : 값이 높으면 빡빡하게, 낮으면 널널하게 객체를 찾음. 보통 기본값으로 0.5를 사용
detector = vision.ObjectDetector.create_from_options(options)

app = FastAPI()

from mediapipe.framework.formats import landmark_pb2
from mediapipe import solutions
import cv2
import time

rendered_image = None
MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # vibrant green

# 추론 결과 내용을 이미지 위에 그리는 함수
def draw_landmarks_on_image(rgb_image, detection_result):
  hand_landmarks_list = detection_result.hand_landmarks
  handedness_list = detection_result.handedness
  annotated_image = np.copy(rgb_image)

  # Loop through the detected hands to visualize.
  for idx in range(len(hand_landmarks_list)):
    hand_landmarks = hand_landmarks_list[idx]
    handedness = handedness_list[idx]

    # Draw the hand landmarks.
    hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    hand_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      hand_landmarks_proto,
      solutions.hands.HAND_CONNECTIONS,
      solutions.drawing_styles.get_default_hand_landmarks_style(),
      solutions.drawing_styles.get_default_hand_connections_style())

    # Get the top left corner of the detected hand's bounding box.
    height, width, _ = annotated_image.shape
    x_coordinates = [landmark.x for landmark in hand_landmarks]
    y_coordinates = [landmark.y for landmark in hand_landmarks]
    text_x = int(min(x_coordinates) * width)
    text_y = int(min(y_coordinates) * height) - MARGIN

    # Draw handedness (left or right hand) on the image.
    cv2.putText(annotated_image, f"{handedness[0].category_name}",
                (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

  return annotated_image

# 추론 후 호출되는 콜백함수
def print_result(result: mp.tasks.vision.HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global rendered_image
    rendered_image = draw_landmarks_on_image(output_image.numpy_view(), result)

options = mp.tasks.vision.HandLandmarkerOptions(
    base_options = mp.tasks.BaseOptions(model_asset_path=f'2.dev\\proj1\\models\\hand_landmarker.task'),
    running_mode = mp.tasks.vision.RunningMode.LIVE_STREAM,
    num_hands = 2, # 감지하는 손의 개수
    result_callback = print_result)

def video_streaming():
    with mp.tasks.vision.HandLandmarker.create_from_options(options) as landmarker:
        # 카메라가 1개면 0, 2개 이상일 경우 1, 2, ... 이렇게 인덱스 형식으로 각각의 카메라를 지정 가능
        cap = cv2.VideoCapture(0) 

        while cap.isOpened():
            # ret : 새로운 프레임을 받아오는 데 성공하면 True
            # fram : 받아온 프레임
            ret, frame = cap.read()

            if ret:
                # 이미지 반전 - 음수:상하좌우, 양수:좌우, 0:상하
                frame = cv2.flip(frame, 1) 

                # 픽셀 데이터를 저장하고 있는 ndarray를 mp.Image 타입으로 변환
                # ndarray : Numpy 라이브러리의 다차원 행렬 자료구조
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame) # SRGB : standard RGB color space

                # 추론하도록 전달
                landmarker.detect_async(mp_image, mp.Timestamp.from_seconds(time.time()).value)
                yield rendered_image
            else:
                print('error')


@app.post("/live_stream/")
async def create_upload_file():
    video_streaming()
    while True:
      if (rendered_image != None):
        return StreamingResponse(rendered_image, media_type="multipart/x-mixed-replace; boundary=frame") 
    

if __name__ == '__main__':
    uvicorn.run('live_stream:app', port = 8001, reload = True)

