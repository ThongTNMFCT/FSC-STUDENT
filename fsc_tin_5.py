#fsc_tin_5
# Dự án 5: Quản lý danh bạ 
danh_ba = {}
while True:
    action = input("Thêm (T), Tìm (Ti), Xóa (X), Hoàn thành (H): ")
    if action == "T":
        ten = input("Nhập tên: ")
        sdt = input("Nhập số điện thoại: ")
        danh_ba[ten] = sdt
    elif action == "Ti":
        ten = input("Nhập tên cần tìm: ")
        print(danh_ba.get(ten, "Không tìm thấy."))
    elif action == "X":
        ten = input("Nhập tên cần xóa: ")
        danh_ba.pop(ten, None)
    elif action == "H":
        break