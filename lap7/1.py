N = int(input("Nhập số nguyên N: "))
if N <= 0:
    print("N phải lớn hơn 0.")
else:
    tran_thi_thanh_thu  = {}
    for i in range(1, N + 1):
        tran_thi_thanh_thu[i] = i ** 3
    print("Từ điển:")
    for key, value in tran_thi_thanh_thu .items():
        print(f"{key}: {value}")
