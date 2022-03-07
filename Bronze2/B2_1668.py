def ascending(items):
    now_max = items[0]
    count = 1
    for item in items:
        if item > now_max:
            count += 1
            now_max = item
    return count


N = int(input())
trophy = []
for j in range(N):
    trophy.append(int(input()))

print(ascending(trophy))
trophy.reverse()
print(ascending(trophy))
