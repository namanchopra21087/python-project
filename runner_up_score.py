if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr=sorted(arr)
    len=len(arr)
    print(arr[len-2])