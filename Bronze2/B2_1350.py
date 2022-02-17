N = int(input())
mylist = list(map(int, input().split()))
size = int(input())
res = 0

for i in mylist:
    if i == 0:
        res += 0
    elif i < size:
        res += size
    else:
        if i % size == 0:
            res += (i // size) * size
        else:
            res += ((i // size) * size) + size
print(res)
