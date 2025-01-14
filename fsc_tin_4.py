#fsc_tin_4
# Dự án 4: Máy phát hiện số nguyên tố
num = int(input("Nhập một số: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} không phải là số nguyên tố.")
            break
    else:
        print(f"{num} là số nguyên tố.")
else:
    print(f"{num} không phải là số nguyên tố.")