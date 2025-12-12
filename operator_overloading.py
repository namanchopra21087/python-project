class Operator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self,other):
        obj3=Operator(self.x*other.x,self.y*other.y)
        return obj3
    def __str__(self):
        return f"({self.x},{self.y})"

obj1=Operator(1,2)
obj2=Operator(3,4)
obj3=obj1*obj2
print(obj3)