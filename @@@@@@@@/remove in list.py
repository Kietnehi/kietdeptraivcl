thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")   # xóa phần tử đầu tiên trong list
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)     # xóa theo index

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # xóa phần tử cuối

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # make the list empty

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
