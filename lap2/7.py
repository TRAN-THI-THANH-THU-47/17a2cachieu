chieu_cao = float(input("nhập chiều cao (m):"))
can_nang = float(input("nhập cân nặng (kg):"))
BMI = can_nang / chieu_cao **2
if BMI < 18.5 :
    print("Gầy")
elif 18.5 < BMI < 24.9 :
    print("Bình thường")
elif 25.0 < BMI < 29.9 :
    print("Hơi béo")
elif BMI > 30.0 :
    print("Béo")