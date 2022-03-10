N = int(input())

for i in range(N):
    fir, sec = input().split('-')

    res = 0
    for j in range(len(fir)):
        res += (ord(fir[j])-65) * (26 ** (len(fir)-j-1))

    if abs(res-int(sec)) <= 100:
        print("nice")
    else:
        print("not nice")
