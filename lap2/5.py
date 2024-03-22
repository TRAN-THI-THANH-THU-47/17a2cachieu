so_luong_nguoi = int(input("Nhập lượng người cùng mua vé xem phim:"))
gia_ve_1_nguoi = 1200000
tong = gia_ve_1_nguoi * so_luong_nguoi
if so_luong_nguoi == 1 :
    print("Tổng số tiền phải trả khi mua vé xem phim là :",tong)
if 2 <= so_luong_nguoi < 4 :
    giam1= 0.05
    print("Tổng số tiền phải trả khi mua vé xem phim là : ",tong -tong * giam1)    
if 4 <= so_luong_nguoi < 10 :
    giam2 = 0.1
    print("Tổng số tiền phải trả khi mua vé xem phim là : ",tong -tong * giam2)  
if so_luong_nguoi >= 10 :
    giam3= 0.2
    print("Tổng số tiền phải trả khi mua vé xem phim là : ",tong -tong * giam3)          