class binary_search:
    def __init__(self,*num):
        self.num=num
    def search(self,number_to_search):
        self.num=sorted(self.num)
        len_of_sorted_list=len(self.num)
        left=0
        right=len_of_sorted_list-1
        while left<=right:
            mid=(left+right)//2
            if self.num[mid]==number_to_search:
                return "Number found at index:",mid
            elif self.num[mid]<number_to_search:
                left=mid+1
            else:
                right=mid-1
        return "Number not found in the list"

def main():
    obj=binary_search(1,2,7,4,5,6,3) #Elements inside list for binary search must be sorted
    result=obj.search(int(input("Enter the number to search:")))
    print(result)
if __name__ == "__main__":
    main()
