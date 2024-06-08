# import cv2
# import math

# DESIRED_HEIGHT = 480
# DESIRED_WIDTH = 480
# IMAGE_FILENAMES = ['burger.jpg', 'cat.jpg']

# def resize_and_show(image):
#   h, w = image.shape[:2]
#   if h < w:
#     img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
#   else:
#     img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))

#   # cv2_imshow(img)
#   cv2.imshow('test', img)
#   cv2.waitKey(0)


# # Preview the images.

# images = {name: cv2.imread(name) for name in IMAGE_FILENAMES}
# for name, image in images.items():
#   print(name)
#   resize_and_show(image)




# STEP 1: Import the necessary modules. 적용하려는 모듈을 import
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision

IMAGE_FILENAMES = ['burger.jpg', 'cat.jpg']

# STEP 2: Create an ImageClassifier object. 다운받은 모델의 상대 주소를 model_asset_path에 설정 후 추론기 생성
base_options = python.BaseOptions(model_asset_path='models\efficientnet_lite0.tflite')
options = vision.ImageClassifierOptions(
    base_options=base_options, max_results=1) # max_resuts : 반환 받으려는 결과 값의 개수
classifier = vision.ImageClassifier.create_from_options(options)

# STEP 3: Load the input image. 추론하려는 데이터 집어넣기
image = mp.Image.create_from_file(IMAGE_FILENAMES[1])

# STEP 4: Classify the input image. 추론 진행
classification_result = classifier.classify(image)

# STEP 5: Process the classification result. In this case, visualize it. 추론 결과 처리
top_category = classification_result.classifications[0].categories[0]
result = f"{top_category.category_name} ({top_category.score:.2f})"

print(result)

# display_batch_of_images(images, predictions)