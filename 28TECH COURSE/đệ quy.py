def dequy(n):
    if n==1 :
        return 1
    if n==0:
        return 0
    return dequy(n-1)+dequy(n-2)

print(dequy(4))