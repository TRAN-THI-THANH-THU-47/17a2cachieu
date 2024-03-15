x1,x2=map(float, input("nhập x1, x2 của vecto a:").split())
y1,y2=map(float, input("nhập y1, y2 của vecto b:").split())

#Phép cộng vecto a + b, phép trừ vecto a – b
phep_cong= x1+y1, x2+y2
phep_tru= x1-y1, x2-y2
print("phép cộng vecto a+b là:", phep_cong)
print("phép trừ vecto a-b là:", phep_tru)

#Độ dài của vecto a, độ dài của vecto b
vecto_a= (x1**2 + x2**2)**(1/2)
vecto_b= (y1**2 + y2**2)**(1/2)
print("độ dài vecto a là:", vecto_a)
print("độ dài vecto_b là:", vecto_b)

#Cosin góc hợp giữa hai vecto a và b (làm tròn đến 2 chữ số thập phân)
tu= x1*x2 + y1*y2
mau= ((x1**2 + y1**2)**(1/2)) * ((x2**2 + y2**2)**(1/2))
cosin=tu/mau
cosin_lam_tron=round(cosin,2)
print("cosin góc hợp giữa hai vecto a và b là:", cosin_lam_tron)