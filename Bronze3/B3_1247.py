from sys import stdin
for i in range(3):
    num = int(stdin.readline())
    res = 0
    for j in range(num):
        res += int(stdin.readline())
    if res == 0:
        print("0")
    elif res > 0:
        print("+")
    else:
        print("-")

