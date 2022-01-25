from sys import stdin
case = int(stdin.readline())
for i in range(case):
    num = int(stdin.readline())
    res = 0
    for j in range(2, 1001):
        N = num
        while True:
            if N % j == 0:
                res += 1
                N //= j
            else:
                break
    print(res)

