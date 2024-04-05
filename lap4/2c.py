print("Tất cả các số Fibonacci nhỏ hơn 1000 là :")
thu = 0
a , b = 0 , 1
while thu < 1000:
    if b >= 1000:
        break
    print(b,end =' , ')
    a,b = b , a + b



