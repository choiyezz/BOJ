num = int(input())
mylist = []
for i in range(num):
    a, b, c = map(int, input().split())
    if a == b == c:
        mylist.append(10000 + 1000*a)
    elif a == b:
        mylist.append(1000 + 100*a)
    elif a == c:
        mylist.append(1000 + 100 * a)
    elif b == c:
        mylist.append(1000 + 100 * b)
    else:
        mylist.append(100 * max(a, b, c))
print(max(mylist))
