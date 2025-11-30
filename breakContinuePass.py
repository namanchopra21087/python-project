available_candies=10
user_input=int(input("Enter number of required candies: "))
i=0
while i<user_input:
    if i>available_candies:
        break
    print("Candie "+str(i))
    i+=1
print("End of break code")
i=0
for i in range(1,10):
    if i%2!=0:
        continue
    if i%2==0:
        pass
    print("Candie "+str(i))
    i+=1
print("End of continue/pass code")