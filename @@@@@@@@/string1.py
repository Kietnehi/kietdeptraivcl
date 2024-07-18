import random
#  ép kiểu dữ liệu
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)
print(random.randrange(1,10)) # random số từ 1--> 9
a="Hello world"
print(a[1])
for x in "concac":
    print(x)
    
a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)    # kiểm tra free có nằm trong chuỗi txt không

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])    # không tính vị trí thứ 5
print(b[5:])
b = "Hello, World!"
print(b[-5:-2])


a.lower()
a.upper()
a.strip()
a="Hello,World"
print(a.replace("H","J")) # thay thế H bằng từ J
print(a.split(","))

a="C"
b="A"
c=a+b   # nối chuỗi


txt = f"The price is {20} x {59} = {20 * 59} dollars"
print(txt)  
# hoặc dùng format
int1=10
int2=10
int3=int1*int2
txt="The price is {int1} *{1}= {2} ".format(int1,int2,int3)
print(txt)    


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)          # chèn watermelon ở vị trí số 3

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
