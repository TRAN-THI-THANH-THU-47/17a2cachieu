n = int(input("Nhập số lượng phần tử: "))
mang_so_nguyen = []

for i in range(n):
  so_nguyen = int(input(f"Nhập phần tử thứ {i + 1}: "))
  mang_so_nguyen.append(so_nguyen)

# In các số nguyên tố
print("Các số nguyên tố trong mảng:")
for so_nguyen in mang_so_nguyen:
  check = True
  for j in range(2, int(so_nguyen**0.5) + 1):
    if so_nguyen % j == 0:
      check = False
      break
  if check:
    print(so_nguyen, end=" ")

# In các số hoàn hảo
print("Các số hoàn hảo trong mảng là:")
for num in mang_so_nguyen:
    tong = 1
    for i in range(2, num):
        if num % i == 0:
            tong += i
    if tong == num:
        print(num)



    