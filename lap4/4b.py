a = 0
S2 = 0
n = int(input("Nhập vào số nguyên n(n>10):"))
if n <= 10:
    print("sai! , vui lòng nhập lại:")
else:
    while a<n:
        S2 += 1/(3**(2*a+1))
        a+=1
print("S2=",S2)