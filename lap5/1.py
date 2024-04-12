so_nguyen_duong = int(input("Nhập số nguyên dương : "))
so_nhi_phan = ' '
while so_nguyen_duong > 0:
  so_du = so_nguyen_duong % 2
  so_nhi_phan = str(so_du) + so_nhi_phan
  so_nguyen_duong //= 2
print("Số nhị phân của số vừa nhập là: ", so_nhi_phan)


