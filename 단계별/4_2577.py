a, b, c = (int(input()) for i in range(3))
mylist = list(0 for j in range(10))

res = str(a * b * c)
for i in res:
    mylist[int(i)] += 1

for i in mylist:
    print(i)
