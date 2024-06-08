import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
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
    base_options = mp.tasks.BaseOptions(model_asset_path='models\\hand_landmarker.task'),
    running_mode = mp.tasks.vision.RunningMode.LIVE_STREAM,
    num_hands = 2, # 감지하는 손의 개수
    result_callback = print_result)

with mp.tasks.vision.HandLandmarker.create_from_options(options) as landmarker:
    # 카메라가 1개면 0, 2개 이상일 경우 1, 2, ... 이렇게 인덱스 형식으로 각각의 카메라를 지정 가능
    cap = cv2.VideoCapture(0) 

    while cap.isOpened():
        # ret : 새로운 프레임을 받아오는 데 성공하면 True
        # fram : 받아온 프레임
        ret, fram = cap.read()

        if ret:
            # 이미지 반전 - 음수:상하좌우, 양수:좌우, 0:상하
            fram = cv2.flip(fram, 1) 

            # 픽셀 데이터를 저장하고 있는 ndarray를 mp.Image 타입으로 변환
            # ndarray : Numpy 라이브러리의 다차원 행렬 자료구조
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=fram) # SRGB : standard RGB color space

            # 추론하도록 전달
            landmarker.detect_async(mp_image, mp.Timestamp.from_seconds(time.time()).value)

            # 완성된 이미지가 있는 경우 렌더링
            if rendered_image is not None:
                cv2.imshow('hand landmarks', rendered_image)
            
            # waitKey에 0을 전달하면 무한 대기, 그 외의 숫자는 그만큼 대기하게 됨
            k = cv2.waitKey(1) & 0xFF 

            # esc 입력 시 종료
            if k == 27: 
                break
        else:
            print('error')
