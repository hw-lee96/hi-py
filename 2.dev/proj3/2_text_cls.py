# docu : https://huggingface.co/docs/transformers/tasks/sequence_classification#inference > Pytorch 예제
# 파이프라인을 전처리 + 후처리 과정으로 분리하여 진행하는 로직
# 실제로 이렇게 사용할 일은 많지 않지만 과정의 이해를 위해 작성 예제 테스트 진행

# 1. 모듈 import
from transformers import pipeline

# 2. 전처리 / 추론 모델 생성
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("stevhliu/my_awesome_model") # 전처리 모델
model = AutoModelForSequenceClassification.from_pretrained("stevhliu/my_awesome_model") # 추론 모델

# step 3. prepare input data (추론하려는 데이터 입력)
text = "This was a masterpiece. Not completely faithful to the books, but enthralling from beginning to end. Might be my favorite of the three."

# step 4. inference
inputs = tokenizer(text, return_tensors="pt") # 전처리 (tokeninzer : 자연어 전처리기)
with torch.no_grad():
    logits = model(**inputs).logits
    # 여기서 후처리하면 되는듯  

# 4-1. preprocessing (data: 사람이 읽을 수 있는 데이터 -> tensor(blob)) : 전처리
# 4-2. inference (tensor(blob) -> logit) : 추론
#.4-3. postprocessing (logit -> data: 사람이 읽을 수 있는 데이터) : 후처리

#  step 5. visualization
print(result)


