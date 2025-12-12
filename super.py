class A:
    def __init__(self):
        print("Inside A")
class B:
    def __init__(self):
        print("Inside B")

class C(A,B):
    def __init__(self):
        print("Inside C")
        super().__init__()

C()