chuoi1 = "Hello"
chuoi2 = "World"

# Khởi tạo chuỗi kết quả
ket_qua = ''

# Xác định độ dài của chuỗi ngắn nhất
min_length = min(len(chuoi1), len(chuoi2))

# Duyệt qua từng ký tự của chuỗi ngắn nhất
for i in range(min_length):
    # Thêm ký tự từ chuỗi thứ nhất
    ket_qua += chuoi1[i]
    # Thêm dấu gạch nối
    ket_qua += '-'
    # Thêm ký tự từ chuỗi thứ hai
    ket_qua += chuoi2[i]

# Nếu một trong hai chuỗi còn dư ký tự, thêm vào kết quả
if len(chuoi1) > min_length:
    ket_qua += chuoi1[min_length:]
if len(chuoi2) > min_length:
    ket_qua += chuoi2[min_length:]

print(ket_qua)
