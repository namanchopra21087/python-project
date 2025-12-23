class Zipped:
    def __init__(self, lst1,lst2):
        self.lst1 = lst1
        self.lst2 = lst2
    def run(self):
        zipped=dict(zip(self.lst1,self.lst2))
        print(zipped)
        for i in zipped:
            print(i,":",zipped[i])

def main():
    zip_obj=Zipped([1,2,3],[4,5,6])
    zip_obj.run()
if __name__=="__main__":
    main()