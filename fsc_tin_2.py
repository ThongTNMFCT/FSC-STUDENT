#fsc_tin_2
# Dự án 2: Đếm số ký tự trong chuỗi
string = input("Nhập chuỗi: ")
letters = sum(c.isalpha() for c in string)
digits = sum(c.isdigit() for c in string)
print(f"Chữ cái: {letters}, Chữ số: {digits}")