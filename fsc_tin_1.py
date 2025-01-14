#fsc_tin_1
# Dự án 1: Máy tính cơ bản
operation = input("Nhập phép tính (+, -, *, /): ")
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Phép tính không hợp lệ!")