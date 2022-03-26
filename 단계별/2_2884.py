H, M = map(int, input().split())
time = H * 3600 + M * 60 - (45 * 60)

hour = time // 3600
if hour < 0:
    hour = 24 + hour

print(hour, (time % 3600) // 60)
