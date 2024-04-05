a = 1
S3 = 0
n = int(input("Nhập vào số nguyên n(n>10):"))
if n <= 10:
    print("sai! , vui lòng nhập lại:")
else:
    while a<=n:
        S3 += (-1)**a*a**2
        a+=1
print("S3=",S3)