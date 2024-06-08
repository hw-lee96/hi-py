import urllib.request # windows에서는 urllib 뒤에 .request를 붙여줘야 함

IMAGE_FILENAMES = ['burger.jpg', 'cat.jpg']

for name in IMAGE_FILENAMES:
  url = f'https://storage.googleapis.com/mediapipe-tasks/image_classifier/{name}'
  urllib.request.urlretrieve(url, name)