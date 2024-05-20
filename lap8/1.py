def so_nguyen_to(num):
  if num <= 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def main():
  
  for num in range(3, 1000, 2):
    if so_nguyen_to(num) and so_nguyen_to(num + 2):
      print(f"{num}, {num + 2}")

if __name__ == "__main__":
  main()
