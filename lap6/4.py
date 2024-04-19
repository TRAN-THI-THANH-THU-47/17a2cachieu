n = int(input("Nhập vào số n: "))
fib_lst = [0, 1]
[fib_lst.append(fib_lst[-1] + fib_lst[-2]) for _ in range(2,n + 1)]
print(fib_lst)
so_nguyen_to = [x for x in range(2, 1000) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print("Danh sách các số nguyên tố nhỏ hơn 1000 là:", so_nguyen_to)