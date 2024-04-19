n = int(input("Nhập kích thước của ma trận vuông: "))
ma_tran = []
print("Nhập các phần tử của ma trận vuông:")
for i in range(n):
    hang = []
    for j in range(n):
        phan_tu = float(input("Nhập phần tử ở hàng {} cột {}: ".format(i + 1, j + 1)))
        hang.append(phan_tu)
    ma_tran.append(hang)

dinh_thuc = ma_tran[0][0] * ma_tran[1][1] - ma_tran[0][1] * ma_tran[1][0]
if dinh_thuc != 0:
    nghich_dao = [[ma_tran[1][1] / dinh_thuc, -ma_tran[0][1] / dinh_thuc], [-ma_tran[1][0] / dinh_thuc, ma_tran[0][0] / dinh_thuc]]
    print("Ma trận nghịch đảo của ma trận đã nhập là:")
    for hang in nghich_dao:
        print(hang)
else:
    print("Ma trận không có ma trận nghịch đảo vì định thức bằng 0.")

doi_xung = True
for i in range(n):
    for j in range(i+1, n):
        if ma_tran[i][j] != ma_tran[j][i]:
            doi_xung = False
            break

if doi_xung:
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận không phải là ma trận đối xứng.")