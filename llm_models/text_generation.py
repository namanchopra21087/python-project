from transformers import pipeline, set_seed

generator=pipeline("text-generation",model="gpt2")
set_seed(42)
print(generator("In this world",top_k=3, max_length=100))