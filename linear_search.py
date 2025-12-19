class LinearSearch:
    def __init__(self,*num):
        self.num=num
    def search(self,number_to_search):
        index=0
        for i in self.num:
            index+=1
            if i==number_to_search:
                return "Number found at element:"+str(index)
        return "Number not found"
def main():
    i1=LinearSearch(11,22,33,44,55,66,77,88)
    user_input=int(input("Enter the number to be searched:"))
    print(i1.search(user_input))
if __name__==main():
    main()