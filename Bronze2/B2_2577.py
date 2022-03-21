from collections import Counter

A = int(input())
B = int(input())
C = int(input())

count = Counter(map(int, str(A * B * C)))
res = [0] * 10

for i in count:
    res[i] = count[i]

for i in res:
    print(i)
