# nhập tọa độ đỉnh 
Mx, My= map(float, input("nhập vào tọa độ đỉnh M(x,y): ").split())
Nx, Ny= map(float, input("nhập vào tọa độ đỉnh N(x,y): ").split())
Px, Py= map(float, input("nhập vào tọa độ đỉnh P(x,y): ").split())
Qx, Qy= map(float, input("nhập vào tọa độ đỉnh Q(x,y): ").split())

# tính toán tọa độ trung điểm mỗi cạnh
MN= (Mx+Nx)/2 , (My+Ny)/2
NP= (Nx+Px)/2 , (Ny+Py)/2
PQ= (Px+Qx)/2 , (Py+Qy)/2
QM= (Qx+Mx)/2 , (Qy+My)/2

# in ra trung điểm mỗi cạnh 
print("trung điểm cạnh MN là: ", MN)
print("trung điểm cạnh NP là: ", NP)
print("trung điểm cạnh PQ là: ", PQ)
print("trung điểm cạnh QM là: ", QM)