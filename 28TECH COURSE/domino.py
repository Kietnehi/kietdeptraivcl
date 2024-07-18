# Nhập hai số nguyên n và m từ người dùng
n, m     = map(int, input().split())

# Kiểm tra nếu n là số chẵn
if n % 2 == 0:
    result = (n / 2) * m
else:
    # Nếu n là số lẻ
    result = (n // 2) * m + (m / 2)

# In kết quả
print(result)

# Tìm giá trị nhỏ nhất trong danh sách
minimum_value = min(1, 2, 3, 4, 5, 6)
print("Giá trị nhỏ nhất là:", minimum_value)

# Tìm giá trị lớn nhất trong danh sách
maximum_value = max(1, 23, 3, 23, 41.213, 123)
print("Giá trị lớn nhất là:", maximum_value)
a= list(map(int,input().split()))
 