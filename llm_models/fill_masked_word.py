from transformers import pipeline, set_seed

fill=pipeline("fill-mask")
print(fill("I am <mask> a great time",top_k=2))