def func1():
    print("Function 1 name is",__name__)

def func2():
    print("Inside function 2")

def main():
    func1()
    func2()

if __name__=="__main__":
    main()

