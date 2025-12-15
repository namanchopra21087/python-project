from threading import Thread
from time import sleep


class A(Thread):
    def run(self):
        for i in range(5):
            print("Inside A")
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(5):
            print("Inside B")
            sleep(1)

def main():
    a=A()
    b=B()
    a.start()
    b.start()
    a.join()        #This shall tell main thread to wait till a joins back
    b.join()        #This shall tell main thread to wait till b joins back
    print("Main Finished")

if __name__=="__main__":
    main()