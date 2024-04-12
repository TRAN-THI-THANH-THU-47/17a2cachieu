chuoi_A = input("Hãy nhập một chuỗi : ")
chuoi_B = input("Hãy nhập một chuỗi : ")
ky_tu_A = set(chuoi_A)
ky_tu_B = set(chuoi_B)
if ky_tu_B.issubset(ky_tu_A):
  so_luong_can_them = len(chuoi_B) - len(chuoi_A)
  if so_luong_can_them >= 0:
    print(f"Có thể chuyển đổi '{chuoi_A}' thành '{chuoi_B}'")
  else:
    print(f"Không thể chuyển đổi '{chuoi_A}' thành '{chuoi_B}'")
else:
  print(f"Không thể chuyển đổi '{chuoi_A}' thành '{chuoi_B}'")