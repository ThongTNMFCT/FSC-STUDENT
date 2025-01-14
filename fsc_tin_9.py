#fsc_tin_9
# Dự án 9: Phân tích dữ liệu từ file CSV
import csv
file_name = input("Nhập tên file CSV: ")
with open(file_name, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    headers = data[0]
    rows = data[1:]
    print(f"Headers: {headers}")
    for row in rows:
        print(row)