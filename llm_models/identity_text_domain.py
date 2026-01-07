from transformers  import  pipeline
4
identify=pipeline("zero-shot-classification")
print(identify("Venezuela president was caught from his home by US Delta forces",
         candidate_labels=['politics','education','business']))
