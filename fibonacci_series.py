#0 1 1 2 3 5 8 13 21 34 ........

def fibonacci_series():
    n=0
    first=0
    second=1
    print(first)
    while n<=10:
        temp=first
        first=second
        second=second+temp
        print(first)
        n=n+1
fibonacci_series()