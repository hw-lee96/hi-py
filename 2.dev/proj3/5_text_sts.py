# docu : https://sbert.net/docs/quickstart.html

# step1
from sentence_transformers import SentenceTransformer

# step 2
model = SentenceTransformer("all-MiniLM-L6-v2")

# step 3
sentence1 = "The weather is lovely today."
sentence2 = "It's so sunny outside!"
sentence3 = "He drove to the stadium."

# step 4
embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)
embedding3 = model.encode(sentence3)

print(embedding1.shape)
print(embedding2.shape)
print(embedding3.shape)

# step 5
similarities = model.similarity(embedding1, embedding2)
print(similarities)