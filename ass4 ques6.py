n = int(input(" enter your number : "))
a = int(input(" enter the number for range to be open : "))
b = int(input(" enter the number for range to be closed : "))
i=0
for i in range(a,b+1) :
    if i%n==0 :
        print(i,end=" ")



