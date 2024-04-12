chuoi = input("Hãy nhập chuỗi các ký tự : ")
dem_ky_tu_dac_biet = {}
tong_so_ky_tu = len(chuoi)
for ky_tu in chuoi:
  if not ky_tu.isalpha() and not ky_tu.isdigit():
    if ky_tu not in dem_ky_tu_dac_biet:
      dem_ky_tu_dac_biet[ky_tu]=0
    dem_ky_tu_dac_biet[ky_tu] += 1
else:
    print("chuỗi không chưa các ký tự đặc biệt")

for ky_tu, so_lan_xuat_hien in dem_ky_tu_dac_biet.items():
  print(f"Ký tự '{ky_tu}' xuất hiện {so_lan_xuat_hien} lần")
  print(f"Tỷ lệ phần trăm: {so_lan_xuat_hien / tong_so_ky_tu * 100}%")


