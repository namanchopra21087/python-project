def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
result=factorial(int(input("Enter a number for which you want to calculate the factorial : ")))
print("Factorial of number is {}".format(result))