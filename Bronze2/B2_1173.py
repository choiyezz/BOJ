N, m, M, T, R = map(int, input().split())
X = m
time = N
count = 0

if m + T > M:
    print(-1)
else:
    while N > 0:
        if X + T <= M:
            X += T
            N -= 1
        else:
            if X - R >= m:
                X -= R
            else:
                X = m
            time += 1
    print(time)
