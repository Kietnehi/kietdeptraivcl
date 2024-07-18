def decimal_to_hexadecimal(n):
    # Trường hợp cơ bản: nếu n bằng 0 thì trả về chuỗi rỗng
    if n == 0:
        return ''
    else:
        # Gọi đệ quy với n chia 16 và lấy ký tự tương ứng với phần dư của n khi chia 16
        result = decimal_to_hexadecimal(n // 16)
        r = n % 16
        if r >= 10:
            result += chr(r + 55)  # 'A' là 65, nhưng 10 tương ứng với 'A' nên 55 + 10 = 65
        else:
            result += str(r)
        return result

# Hàm chính để chạy và kiểm tra
number = 100
hex_representation = decimal_to_hexadecimal(number)
# Trường hợp n bằng 0 thì trả về "0"
hex_representation = '0' if hex_representation == '' else hex_representation
print(f"Số {number} trong hệ thập lục phân là: {hex_representation}")
