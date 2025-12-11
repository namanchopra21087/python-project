from functools import reduce

num=[43,88,1,3,9,43]
even=list(filter(lambda x:x%2==0,num))
double=list(map(lambda x:x*2,num))
sums=reduce(lambda x,y:x+y,double)


print(even)
print(double)
print(sums)