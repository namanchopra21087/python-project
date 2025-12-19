class bubble_sort:
    def __init__(self,num):
        self.num=num
    def sort(self):
        num_length=len(self.num)
        for i in range(num_length):
            swap=False
            for j in range(num_length-i-1):
                if self.num[j]>self.num[j+1]:
                    self.num[j],self.num[j+1]=self.num[j+1],self.num[j]
                    swap=True
            if not swap:
                break
        return "Sorting finished"
def main():
    lst=[3,4,1,3,2,7,5,3]
    obj=bubble_sort(lst)
    result=obj.sort()
    print(result)
    print(obj.num)
if __name__=="__main__":
    main()

