
def is_odd(x):
  return x % 2 != 0

def odd_numbers(numbers):
  return list(filter(is_odd, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = odd_numbers(numbers)
print(odd_numbers) 

def is_even(x):
  
  return x % 2 == 0

def even_numbers(numbers):
  
  return list(filter(is_even, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = even_numbers(numbers)
print(even_numbers)  

def binh_phuong(x):

  return x * x * x

def main():

  danh_sach_ban_dau = [1, 2, 3, 4, 5]

  danh_sach_lap_phuong = map(binh_phuong, danh_sach_ban_dau)

  danh_sach_lap_phuong = list(danh_sach_lap_phuong)

  print(danh_sach_lap_phuong)


def binh_phuong(x):
  return x * x * x

def chan(x):
  return x % 2 == 0

so_nguyen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

so_chan = list(filter(chan, so_nguyen))

lap_phuong_so_chan = list(map(binh_phuong, so_chan))

print(lap_phuong_so_chan)


def binh_phuong(x):
  
  return x * x * x

def la_so_le(x):

  return x % 2 != 0

so_nguyen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

so_le = list(filter(la_so_le, so_nguyen))

so_le_binh_phuong = list(map(binh_phuong, so_le))

print(so_le_binh_phuong)

if __name__ == "__main__":
  main()