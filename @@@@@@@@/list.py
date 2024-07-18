thisList=["con cac ","hello", " hi"]
del thisList[1]
del thisList    
thisList.clear()
len(thisList)
type(thisList)
print(thisList[2:5])
print(thisList[2:])
print(thisList[:5])
print(thisList[-4:-1])

for x in thisList:
    print(x)
    
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thisList.sort()
thisList.sort(reverse=True)

# sắp xếp theo những số gần với 50 nhất 
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thisList.reverse()

# sắp xếp không phân biệt chữ hoa chữ thường
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

