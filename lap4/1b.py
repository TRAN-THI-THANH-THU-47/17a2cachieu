tong = 0
so_chan = " "
while tong <= 1000:
  so = int(input("Nhập số nguyên dương: "))
  tong += so

  if so %2==0:
    so_chan += str(so) + " "
print("b) Các số chẵn đã vừa nhập:", so_chan)


