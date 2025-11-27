#Option 1
x=5
y=6
x=x+y
y=x-y
x=x-y
print("Numbers after swap with option 1:",x,y)
#Option 2
x=5
y=6
x=x^y
y=x^y
x=x^y
print("Numbers after swap with option 2:",x,y)
#Option 3
x=5
y=6
x,y=y,x
print("Numbers after swap with option 3:",x,y)