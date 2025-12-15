class TopTen:
    def __init__(self):
        self.num=[22,55,77,66]
    def check_yield(self):
        yield 1
        yield 2
        yield 3
        yield 4
        yield 5
def it_func():
    print("Inside iterator")
    obj=TopTen()
    it=iter(obj.num)
    i=0
    while i< len(obj.num):
        print(it.__next__())
        i+=1

def yield_func():
    print("Inside Yield")
    obj=TopTen()
    yt=obj.check_yield()
    i=0
    for item in yt:
        print(item)
def main():
    it_func()
    yield_func()
if __name__=="__main__":
    main()