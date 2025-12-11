#Define inner class method outside outer class
class Computer:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

    class Laptop:
        def __init__(self,memory):
            self.memory=memory

comp=Computer("Laptop")
lap=comp.Laptop(77)

print(lap.memory)
print(comp.name)

