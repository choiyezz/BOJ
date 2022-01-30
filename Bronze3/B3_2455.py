res = 0
mylist = []
for i in range(4):
    pout, pin = map(int, input().split())
    res = res + pin - pout
    mylist.append(res)
print(max(mylist))
