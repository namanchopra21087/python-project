from numpy import *
from numpy.ma.core import append

arr=array([])
x=int(input("Enter number of elements inside array:"))

for i in range(0,x):
    arr=append(arr,int(input("Enter element:")))

search_ele=int(input("Enter element to be searched:"))

for i in range(0,x):
    if arr[i]==search_ele:
        print("Element found at index",i)
        break
else:
    print("Element not found")
