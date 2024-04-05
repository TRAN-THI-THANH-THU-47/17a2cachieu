a = 1
S1 = 0
n = int(input("Nhập n (n > 10): "))
if n <= 10:
    print("sai , vui lòng nhập lại:")
while a <= n:
    S1 += 6**a
    a += 1
print(f"a)Tổng S1 = {S1}")