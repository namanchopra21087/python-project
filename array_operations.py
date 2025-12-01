from numpy import *

arr=array([2,3,4,5,6,2,8])

print("Max",max(arr))
print("Min",min(arr))
print("Sum",sum(arr))
print("Sort",sort(arr))

print("Copy by reference or Shallow Copy")
arr1=array([2,3,4,5,6,2,8])
arr2=arr1
arr1[2]=9
print(arr1)
print(arr2)

print("Copy independently or Deep Copy")
arr3=arr1.copy()
arr1[2]=10
print(arr1)
print(arr3)

print("Add value to each element of array")
arr3=arr3+5
print(arr3)

print("Multiply two arrays")
print(arr1*arr3)
