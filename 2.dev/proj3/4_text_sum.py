# 텍스트 요약
# 1.import
from transformers import pipeline

# 2. create inference instance
summarizer = pipeline("summarization", model="stevhliu/my_awesome_billsum_model")

# 3. input data
text = "summarize: The Inflation Reduction Act lowers prescription drug costs, health care costs, and energy costs. It's the most aggressive action on tackling the climate crisis in American history, which will lift up American workers and create good-paying, union jobs across the country. It'll lower the deficit and ask the ultra-wealthy and corporations to pay their fair share. And no one making under $400,000 per year will pay a penny more in taxes."

# 4. inference
result = summarizer(text)

#  step 5. visualization
print(result)
