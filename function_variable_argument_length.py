#Key value variable length argument
def func(**kw_data):
    for i,j in kw_data.items():
        print(i,j)
func(a=1,b='2',c=3.0)

#Default argument value
def func2(a,b=10):
    print(a,b)
func2(100)

#Variable length argument
def func3(a, *b):
    print(a,b)
    for i in b:
        print(i)
func3('test',1,3,7)

#Passing key with value in function argument
def func4(age,name):
    print(age,name)
func4(name='naman',age=10)