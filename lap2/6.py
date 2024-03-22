x=float(input("nhap so nguyen thu 1:"))
y=float(input("nhap so nguyen thu 2:"))
z=float(input("nhap so nguyen thu 3:"))
if x > y and x < z :
    print("Số lớn thứ hai là : ",x)
elif x<y and x>z :
    print("Số lớn thứ hai là : ",x)
elif y > x and y < z : 
    print("Số lớn thứ hai là : ",y)
elif y < x and y > z :
    print("Số lớn thứ hai là : ",y)
elif z > x and z < y :
    print("Số lớn nhất là : ",z)
elif z < x and z > y :
    print("Số lớn thứ hai là : ",z)


