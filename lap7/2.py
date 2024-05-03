
sinh_vien = {}
for i in range(1, 11):
    ten = input(f"Nhập tên của sinh viên {i}: ")
    diem = float(input(f"Nhập điểm của sinh viên {i}: "))
    sinh_vien[ten] = diem
thong_ke = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for ten, diem in sinh_vien.items():
    if diem < 4.0:
        thong_ke['F'] += 1
    if 4.0 <= diem < 5.5:
        thong_ke['D'] += 1
    if 5.5 <= diem < 7.0:
        thong_ke['C'] += 1
    if 7.0 <= diem < 8.5:
        thong_ke['B'] += 1
    else:
        thong_ke['A'] += 1
print("Kết quả thống kê số lượng sinh viên theo loại học lực:")
for loai_diem, so_luong in thong_ke.items():
    print(f"Loại {loai_diem}: {so_luong} sinh viên")
