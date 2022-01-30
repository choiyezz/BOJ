res = 0
mylist = []
for i in range(10):
    pout, pin = map(int, input().split())
    res = res + pin - pout
    mylist.append(res)
print(max(mylist))
