# docu : https://huggingface.co/docs/transformers/tasks/sequence_classification

# step 0
# - 1. pip 인스톨 진행 : pip install transformers
#
# - 2. pyTorch 관련 에러 해결 : https://pytorch.org/get-started/locally/ 이동
# - 각자의 환경, OS 등을 고려하여 옵션 선택
# - ex) stable > windows > conda > python > cpu > run this command 로 install 진행
# - 현재 인터넷 상황이 좋지 않아서 cpu를 선택함. 이후 개발 시에는 CUDA를 사용해야 GPU를 활용한 처리가 가능하다.
#
# - 3. chardet 관련 에러 발생. 에러 로그에는 나오지 않지만 의존되는 부분이 있어서 설치 필요
# - pip install chardet 
#
# - 4. inference 예제 테스트

# step 1. import modules (모듈 다운로드)
from transformers import pipeline

# step 2. create inference instance (추론 객체 생성)
# (태스크 명, '{작성자 명}/{모델 명}')
classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")

# step 3. prepare input data (추론하려는 데이터 입력)
text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."

# step 4. inference (추론 진행)
result = classifier(text)

#  step 5. visualization (결과 내용 시각화)
print(result)
