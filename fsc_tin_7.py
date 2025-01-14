#fsc_tin_7
# Dự án 7: Tạo mật khẩu ngẫu nhiên
import random
import string
dai = int(input("Nhập độ dài mật khẩu: "))
mat_khau = ''.join(random.choices(string.ascii_letters + string.digits, k=dai))
print(f"Mật khẩu của bạn: {mat_khau}")