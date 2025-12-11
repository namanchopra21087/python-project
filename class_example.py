class Car:
    #Global Variable
    wheels=4
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print(self.make,self.model,self.year,self.wheels)

#Maruti car object instantiated
car1=Car("Maruti","swift",2025)
car1.display()

#Mercedes car object instantiated
car2=Car("Mercedes","honda",2026)
car2.display()

Car.wheels=5
car2.display()