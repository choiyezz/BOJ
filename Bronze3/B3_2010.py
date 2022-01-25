from sys import stdin
num = int(stdin.readline())
res = 0
for i in range(num):
    res += (int(stdin.readline()) - 1)
print(res + 1)
