x,z=map(float, input("nhập vào hai số thực:").split())
e= 2.718281828
import math 
tu= ((x**2) * math.sin(z)) + (abs(x))**(1/2)
mau= math.log(z) + e**(x-1)
f= tu/mau + math.atan(x*z)
print("giá trị của biểu thức f(x,z) là:",round(f,2))
