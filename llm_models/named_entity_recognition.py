from transformers import pipeline

ner=pipeline("ner", model="dslim/bert-base-NER",aggregation_strategy="simple")
print(ner("I am Naman Chopra and I worked at Happiest-Minds and I stay in Delhi"))