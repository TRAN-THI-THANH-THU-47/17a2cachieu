import random
import csv

# 1. Tạo một list để lưu trữ 10 màu bóng khác nhau.
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Black", "White", "Pink", "Brown"]

# 2. Tạo một set để lưu trữ các màu bóng đã được rút ra.
drawn_colors = set()

# 3. Tạo một dictionary để lưu trữ số lượng bóng của mỗi màu.
ball_count = {color: 1 for color in colors}

# 4. Viết các hàm để thực hiện các chức năng chính.

def draw_ball():
    """Rút một bóng từ hộp."""
    if sum(ball_count.values()) == 0:
        raise ValueError("No balls left to draw!")
    ball = random.choice([color for color, count in ball_count.items() if count > 0])
    ball_count[ball] -= 1
    drawn_colors.add(ball)
    return ball

def calculate_probability(color):
    """Tính xác suất rút được bóng của một màu cụ thể."""
    total_balls = sum(ball_count.values())
    if total_balls == 0:
        return 0
    return ball_count[color] / total_balls

def display_remaining_balls():
    """Hiển thị số lượng bóng còn lại trong hộp."""
    for color, count in ball_count.items():
        print(f"{color}: {count}")

def save_results_to_csv(results):
    """Lưu lại kết quả của quá trình rút bóng vào một file CSV."""
    with open('draw_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Drawn Color", "Probability", "Remaining Balls"])
        for result in results:
            writer.writerow(result)

# 6. Lặp lại quá trình rút bóng 5 lần.
results = []
for _ in range(5):
    drawn_ball = draw_ball()
    prob = calculate_probability(drawn_ball)
    remaining_balls = {color: count for color, count in ball_count.items()}
    results.append([drawn_ball, prob, remaining_balls])
    print(f"Drawn Ball: {drawn_ball}")
    print(f"Probability of Drawing {drawn_ball}: {prob:.2f}")
    display_remaining_balls()
    print("-------------------------")

# Kiểm tra điều kiện chiến thắng
color_counts = {color: sum(1 for result in results if result[0] == color) for color in colors}
if any(count >= 3 for count in color_counts.values()):
    print("Người chơi chiến thắng khi rút được 5 bóng có 3/5 màu giống nhau!")
else:
    print("Người chơi không chiến thắng.")

# 7. Lưu lại kết quả của quá trình rút bóng vào một file CSV.
save_results_to_csv(results)