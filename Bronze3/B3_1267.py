num = int(input())
call = list(map(int, input().split()))
res1 = res2 = 0

for i in range(num):
    res1 += 10 * ((call[i] // 30) + 1)
    res2 += 15 * ((call[i] // 60) + 1)

if res1 > res2:
    print("M", res2)
elif res1 < res2:
    print("Y", res1)
else:
    print("Y", "M", res1)
