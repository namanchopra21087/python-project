import math


def is_leap(year):
    leap = False
    if year>=1900 and year <=math.pow(10,5):
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            leap = True

    return leap

if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))