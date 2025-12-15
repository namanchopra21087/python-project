class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show(self):
        print("Inside A")
class B(A):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show(self):
        print("Inside B")
obj_b=B(1,2)
obj_b.show()