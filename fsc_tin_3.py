#fsc_tin_3
# Dự án 3: Trò chơi đoán số
import random
number = random.randint(1, 100)
while True:
    guess = int(input("Đoán một số từ 1 đến 100: "))
    if guess < number:
        print("Số bạn đoán nhỏ hơn.")
    elif guess > number:
        print("Số bạn đoán lớn hơn.")
    else:
        print("Chính xác! Bạn đoán đúng.")
        break