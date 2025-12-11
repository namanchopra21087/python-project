class A:
    def show(self):
        print("Inside A")
class B(A):
    def show(self):
        print("Inside B")
class C(A):
    def show(self):
        print("Inside C")
class D(B,C):
    pass

d=D()
d.show()