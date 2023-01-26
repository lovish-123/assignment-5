lista = []
for i in range(1,11):
    n = int(input(f"integer value {i} : "))
    lista.append(n)
print(lista)

for j in lista:
    if j>0:
        print("positive numbers are : ",j)
    elif j<0 :
        print("negative numbers are : ",j)
    elif j%2!=0 :
        print("odd numbers are : ",j)
    elif j%2==0:
        print("even numbers are : ",j)





