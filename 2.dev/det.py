import cv2
import numpy as np

MARGIN = 10  # pixels
ROW_SIZE = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # red

IMAGE_FILE = 'cat_and_dog.jpg'
# IMAGE_FILE = 'animals.jpg'

import cv2

# img = cv2.imread(IMAGE_FILE)
# cv2.imshow('test', img)
# cv2.waitKey(0)

def visualize(
    image,
    detection_result
) -> np.ndarray:
  """Draws bounding boxes on the input image and return it.
  Args:
    image: The input RGB image.
    detection_result: The list of all "Detection" entities to be visualize.
  Returns:
    Image with bounding boxes.
  """
  for detection in detection_result.detections:
    # Draw bounding_box
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, TEXT_COLOR, 3)

    # Draw label and score
    category = detection.categories[0]
    category_name = category.category_name
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (MARGIN + bbox.origin_x,
                     MARGIN + ROW_SIZE + bbox.origin_y)
    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                FONT_SIZE, TEXT_COLOR, FONT_THICKNESS)

  return image



# STEP 1: 필요한 모듈 가져오기
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: 추론기 객체 생성
base_options = python.BaseOptions(model_asset_path='models\efficientdet_lite0.tflite')
options = vision.ObjectDetectorOptions(base_options=base_options,
                                       score_threshold=0.5) # score_threshold : 값이 높으면 빡빡하게, 낮으면 널널하게 객체를 찾음. 보통 기본값으로 0.5를 사용
detector = vision.ObjectDetector.create_from_options(options)

# STEP 3: 추론기에 입력할 이미지 생성(가져오기)
image = mp.Image.create_from_file(IMAGE_FILE)

# STEP 4: 입력한 이미지 추론 진행
detection_result = detector.detect(image)

# STEP 5: 추론 결과 처리. 시각화 진행
image_copy = np.copy(image.numpy_view()) # 원본 이미지를 카피
annotated_image = visualize(image_copy, detection_result) # 복사한 이미지에 결과 값을 그리기
rgb_annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB) # 이미지를 다시 반전
cv2.imshow('test', rgb_annotated_image)
cv2.waitKey(0)