print("Nhập thông số của đường thẳng thứ nhất:")
a1 = float(input("Nhập hệ số a1: "))
b1 = float(input("Nhập hệ số b1: "))
c1 = float(input("Nhập hệ số c1: "))

print("Nhập thông số của đường thẳng thứ hai:")
a2 = float(input("Nhập hệ số a2: "))
b2 = float(input("Nhập hệ số b2: "))
c2 = float(input("Nhập hệ số c2: "))

# Kiểm tra 
if a1/a2 == b1/b2 == c1/c2:
    print("Hai đường thẳng là đồng quy")

elif a1 * a2 + b1 * b2 == 0:
    print("Hai đường thẳng là vuông góc")
else:
    print("Hai đường thẳng là song song hoặc cắt nhau")
