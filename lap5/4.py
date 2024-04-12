ky_tu_so = "0123456789"
chuoi = input("Nhập chuỗi ký tự: ")
chuoi_so = ''
for thu in chuoi:
  if thu in ky_tu_so:
    chuoi_so += thu
if chuoi_so == '':
  print("Chuỗi không chứa số nào!")
  exit()
so = int(chuoi_so)
nguyen_to = True
if so <= 1:
  nguyen_to = False
else:
  for i in range(2, int(so**0.5) + 1):
    if so % i == 0:
      nguyen_to = False
      break
if nguyen_to:
  print(f"{so} là số nguyên tố.")
else:
  print(f"{so} không phải là số nguyên tố.")
