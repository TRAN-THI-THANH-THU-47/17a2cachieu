a = 0
S4 = 0
n = int(input("Nhập vào số nguyên n(n>10):"))
if n <= 10:
    print("sai , vui lòng nhập lại:")
else:
    while a<n:
        S4 += a*(a + 1)*(a + 2 )
        a+=1
print("S4=",S4)