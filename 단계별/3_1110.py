N = int(input())    # 26
M = N
count = 0

while True:
    a = N // 10         # 2
    b = N % 10          # 6
    c = (a + b) % 10    # 2 + 6 = 8
    N = (b * 10) + c    # 60 + 8

    count += 1
    if N == M:
        break
print(count)
