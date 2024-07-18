thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

i=0
while i < len(thislist):
    print(thislist[i])
    i+=1

a= 36
b="hello"
c=f"{b} {a}"
d="{0} {1}".format(a,b)
print(c)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)