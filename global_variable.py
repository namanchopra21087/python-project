a=16

def variable_global_local():
    a=15
    x=globals()['a']
    print("In method",a,x)

variable_global_local()
print("Outside method",a)