def cal_per(x,y,z,num):
    per=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)if not i+j+k==num]
    print(per)
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    cal_per(x,y,z,n)