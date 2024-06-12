# step 1. import modules
from transformers import pipeline

# step 2. create inference instance (추론 객체 생성)
# (태스크 명, '{작성자 명}/{모델 명}')
# classifier = pipeline("sentiment-analysis", model="stevhliu/my_awesome_model")

# 한글 가능 모델 사용
# classifier = pipeline("sentiment-analysis", model="snunlp/KR-FinBert-SC")

# text summarization
# classifier = pipeline("sentiment-analysis", model="Falconsai/text_summarization")

# token classification
# classifier = pipeline("sentiment-analysis", model="dslim/bert-base-NER")

# question answering - kr
classifier = pipeline("sentiment-analysis", model="timpal0l/mdeberta-v3-base-squad2")
# step 3. prepare input data (추론하려는 데이터 입력)
text = '맛이 없을래야 없을 수가 없다.'

# step 4. inference
result = classifier(text)

#  step 5. visualization
print(result)
