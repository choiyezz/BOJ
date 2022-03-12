num = int(input())
start = num - (len(str(num)) * 9)
start = 1 if start < 1 else start

ans = 0
for i in range(start, num+1):
    res = sum(map(int, str(i)))
    if num == (i + res):
        ans = i
        break
print(ans)
