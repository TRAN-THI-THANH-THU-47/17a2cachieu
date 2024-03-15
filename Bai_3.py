retained=10000
interest=0.06

# tính toán số tiền sẽ có sau 5 năm và lưu kết quả vào biến amount_after_5_years
amount_after_5_years= retained *((1.0+interest)**5)

# tính toán số tiền sẽ có sau 10 năm và lưu kết quả vào biến amount_after_10_years
amount_after_10_years= retained *((1.0+interest)**10)

# tính toán tỉ lệ tăng trưởng của số tiền bạn sẽ có sau 10 năm so với số tiền bạn sẽ có sau 5 năm và lưu kết quả vào biến growth_rate 
growth_rate= (amount_after_10_years - amount_after_5_years) / amount_after_5_years

# in kết quả tất cả các phép toán 
print("số tiền nhận được sau 5 năm là:", amount_after_5_years)
print("số tiền nhận được sau 10 năm là:", amount_after_10_years)
print("tỷ lệ tăng trưởng là:", growth_rate)