from transformers import pipeline

sa=pipeline("sentiment-analysis")
flag="Y"
while flag.upper()=="Y":
    choice=input("Do you want to enter single text or list of text for analysis: S or L")
    if choice.upper()=="S":
        text=input("Enter text:")
        print(sa(text))
        flag=input("Do you want to continue Y/N")
    elif choice.upper()=="L":
        user_enters="Y"
        lst=[]
        while user_enters.upper()=="Y":
            text=input("Enter list element:")
            lst.append(text)
            user_enters=input("Do you want to add more elements Y/N")
        print(sa(lst))
        flag=input("Do you want to continue Y/N")


