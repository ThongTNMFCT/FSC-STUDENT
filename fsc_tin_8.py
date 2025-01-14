#fsc_tin_8
# Dự án 8: Trình quản lý file
import os
while True:
    action = input("Xem (X), Sao chép (S), Xóa (Xo), Đổi tên (D), Hoàn thành (H): ")
    if action == "X":
        print(os.listdir())
    elif action == "S":
        nguon = input("Nhập file nguồn: ")
        dich = input("Nhập file đích: ")
        with open(nguon, 'rb') as f1, open(dich, 'wb') as f2:
            f2.write(f1.read())
    elif action == "Xo":
        ten_file = input("Nhập tên file cần xóa: ")
        os.remove(ten_file)
    elif action == "D":
        cu = input("Nhập tên file hiện tại: ")
        moi = input("Nhập tên file mới: ")
        os.rename(cu, moi)
    elif action == "H":
        break