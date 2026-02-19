from collections import Counter

def find_occurence():
    lst_char=list(input())
    dict_char=Counter(lst_char)
    sorted_items =sorted(dict_char.items(),key=lambda x:(-x[1],x[0]))
    for char,count in sorted_items[:3]:
        print(char,count)

if __name__ == "__main__":
    find_occurence()