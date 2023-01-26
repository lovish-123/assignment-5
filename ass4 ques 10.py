a = int(input("ENTER THE NUMBER TO OPEN THE RANGE : "))
b = int(input("ENTER THE NUMBER TO CLOSE THE RANGE : "))
for i in range(a,b+1):
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)








