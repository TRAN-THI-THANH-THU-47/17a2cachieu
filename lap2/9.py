print("Nhập thông số của đường thẳng:")
a = float(input("Nhập hệ số góc a: "))
b = float(input("Nhập hệ số tự do b: "))

print("Nhập thông số của đường tròn:")
x_tam = float(input("Nhập tọa độ x của tâm đường tròn: "))
y_tam = float(input("Nhập tọa độ y của tâm đường tròn: "))
ban_kinh = float(input("Nhập bán kính của đường tròn: "))

khoang_cach = abs(a*x_tam + b*y_tam) / (a**2 + b**2)**0.5

if khoang_cach < ban_kinh:
    print("Đường thẳng cắt đường tròn")
elif khoang_cach == ban_kinh:
    print("Đường thẳng tiếp xúc đường tròn")
elif khoang_cach > ban_kinh:
    print("Đường thẳng nằm ngoài đường tròn")
else:
    print("Đường thẳng nằm trong đường tròn")