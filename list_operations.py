if __name__ == '__main__':
    ele_lst=[]
    n=int(input("Enter number of commands to be inserted:"))
    for i in range(n):
        command=input(f"Enter command {i+1}: ")
        spe_lst = command.split()
        if spe_lst[0] == "insert":
            ele_lst.insert(int(spe_lst[1]),int(spe_lst[2]))
        elif spe_lst[0] == "append":
            ele_lst.append(int(spe_lst[1]))
        elif spe_lst[0] == "print":
            print(ele_lst)
        elif spe_lst[0] == "sort":
            ele_lst.sort()
        elif spe_lst[0] == "pop":
            ele_lst.pop()
        elif spe_lst[0] == "reverse":
            ele_lst.reverse()
        elif spe_lst[0] == "remove":
            ele_lst.remove(int(spe_lst[1]))
