day_so = input("Nhập dãy số, cách nhau bằng dấu cách: ").split()
day_so = [float(x) for x in day_so]
so_lon_nhat = max(day_so)
so_nho_nhat = min(day_so)
print("Số lớn nhất trong dãy số là:", so_lon_nhat)
print("Số nhỏ nhất trong dãy số là:", so_nho_nhat)
