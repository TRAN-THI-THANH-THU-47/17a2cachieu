n = int(input("Hãy nhập số nguyên dương : "))
# a
if n <= 0 :
    print("Hãy nhập lại !")
so_cac_so_hang = (n - 1) / 1 + 1
S1 = (1 + n) * so_cac_so_hang / 2
print("S1 = ",S1)

# b
S2 = 0
for n in range(1, n + 1):
    S2 = S2 + 1/n
print("S2 = ",S2)

# c
S3 = 0
for n in range(1, n + 1):
    S3 = S3 + (1/(2*n)**0.5)
print("S3 = ",S3)

# d
S4 = 0
for n in range(1, n + 1):
    S4 = S4 + (((-1) ** (n + 1)) / n)
print("S4 = ",S4)
