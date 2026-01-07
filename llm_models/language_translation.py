from transformers import pipeline
trans=pipeline("translation",model="Helsinki-NLP/opus-mt-en-hi")
print(trans("In this beautiful world, green grass blue skies, I love a bit of a sun shine"))