import math
a = float(input("the first side of triangle is : "))
b = float(input("the second side of triangle is : "))
c = float(input("the third side of triangle is : "))
s = a+b+c/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
if  a ==0 or b==0 or c==0 :
    print("the triangle is not possible!!")
else :
    print("area of the triangle is : ",area)