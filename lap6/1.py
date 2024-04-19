mang_so_nguyen = []
tong_chan = 0
tong_le = 0
phan_tu = int(input("Nhập số lượng phần tử: "))
for i in range(phan_tu):
  so_nguyen = int(input(f"Nhập phần tử thứ {i + 1}: "))
  mang_so_nguyen.append(so_nguyen)
for so in mang_so_nguyen:
  if so % 2 == 0:
    tong_chan += so
for so in mang_so_nguyen:
  if so % 2 != 0:
    tong_le += so
print("Mảng số nguyên đã nhập:" ,mang_so_nguyen)
print("Tổng của tất cả các số chẵn trong mảng:" , tong_chan)
print("Tổng của tất cả các số chẵn trong mảng: ", tong_le )
