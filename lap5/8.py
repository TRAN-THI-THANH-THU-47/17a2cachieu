n = input("Hãy nhập chuỗi gồm 10 ký tự :")
print("Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8 là : ")
print(n[1:8])

print(" Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5 là : ")
print(n[4:])

print("Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự là : ")
print(n[:6:-1])

print("Chuyển đổi các ký tự trong chuỗi thành chữ thường là : ")
print(n.lower())

print("Chuyển đổi các ký tự trong chuỗi thành chữ hoa là : ")
print(n.upper())

print("Đảo ngược chuỗi ký tự vừa nhập là : ")
print(n[::-1])
