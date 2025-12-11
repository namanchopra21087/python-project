#Define inner class method inside outer class
class Computer:
    def __init__(self,name,memory):
        self.name=name
        self.lap=self.Laptop(memory)
    def display(self):
        print(self.name)

    class Laptop:
        def __init__(self,memory):
            self.memory=memory

comp=Computer("Laptop",67)

print(comp.lap.memory)