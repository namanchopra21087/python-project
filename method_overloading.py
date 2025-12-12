class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    #Method overloading is nto directly supported in python. Its done rather with below trick
    def add(self,x,y,z=0):
        return x+y+z
a_obj=A(1,2)
print(a_obj.add(3,4))
print(a_obj.add(3,4,5))