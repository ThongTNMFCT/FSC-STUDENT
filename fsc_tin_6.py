#fsc_tin_6
# Dự án 6: Tạo lịch sự kiện
import datetime
lich_su_kien = []
while True:
    action = input("Thêm (T), Xem (X), Hoàn thành (H): ")
    if action == "T":
        ten_su_kien = input("Nhập tên sự kiện: ")
        ngay = input("Nhập ngày (YYYY-MM-DD): ")
        lich_su_kien.append((ten_su_kien, ngay))
    elif action == "X":
        for sk in lich_su_kien:
            print(f"{sk[0]}: {sk[1]}")
    elif action == "H":
        break
