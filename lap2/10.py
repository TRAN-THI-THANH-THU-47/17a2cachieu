print("Danh sách thể loại phim:")
print("1. Hành động")
print("2. Kinh dị")
print("3. Tình cảm")
print("4. Hài hước")
print("5. Hoạt hình")

the_loai = int(input("Nhập số tương ứng với thể loại phim bạn muốn xem: "))

thoi_gian = input("Nhập thời gian muốn xem phim (sáng, trưa, chiều, tối): ")

if the_loai== 3:
    if thoi_gian == "tối" :
      print("Phim được chiếu vào lúc 21h")
    else :
       print("Không có suất chiếu")
if the_loai== 5:
    if thoi_gian == "sáng" :
      print("Chương trình được chiếu vào lúc 5h sáng")
    elif thoi_gian == "trưa":
       print("Chương trình được chiếu vào lúc 12h30 trưa")
    else :
       print("Không có suất chiếu")
if the_loai == 2:
    if thoi_gian == "tối":
      print("Chương trình được chiếu vào lúc 23h tối")
    else :
      print("không có suất chiếu")
if the_loai == 1:
    print("không có suất chiếu")