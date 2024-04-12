

chuoi = input("Nhập chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")
vi_tri = chuoi.find(tu_can_tim)
so_lan_xuat_hien = 0
while vi_tri != -1:
  so_lan_xuat_hien += 1
  vi_tri = chuoi.find(tu_can_tim, vi_tri + len(tu_can_tim))
print(f"Vị trí đầu tiên của từ '{tu_can_tim}' trong chuỗi là: {vi_tri}")
print(f"Số lần xuất hiện của từ '{tu_can_tim}' trong chuỗi là: {so_lan_xuat_hien}")
danh_sach_tu = chuoi.split()
so_lan_xuat_hien_thu= {}
for tu in danh_sach_tu:
  vi_tri = chuoi.find(tu)
  so_lan_xuat_hien = 0
  while vi_tri != -1:
    so_lan_xuat_hien += 1
    vi_tri = chuoi.find(tu, vi_tri + len(tu))
  so_lan_xuat_hien_thu[tu] = so_lan_xuat_hien
tu_xuat_hien_nhieu_nhat = max(so_lan_xuat_hien_thu, key=so_lan_xuat_hien_thu.get)
print(f"Từ xuất hiện nhiều nhất trong chuỗi là: '{tu_xuat_hien_nhieu_nhat}' với {so_lan_xuat_hien_thu[tu_xuat_hien_nhieu_nhat]} lần xuất hiện")
