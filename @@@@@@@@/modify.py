a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a.strip()       # xóa khoảng trống 

a = "Hello, World!"
print(a.replace("H", "J"))  # đổi chữ H thành chữ J 

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']  
# tách thành mảng những chỗ có dấu phẩy

age="concac"+a
print(age)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

