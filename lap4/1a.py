tong = 0
so_le = " "
while tong <= 1000:
  so = int(input("Nhập số nguyên dương: "))
  tong += so

  if so %2!=0:
    so_le += str(so) + " "
print("a) Các số lẻ đã vừa nhập:", so_le)


