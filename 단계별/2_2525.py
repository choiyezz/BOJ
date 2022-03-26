H, M = map(int, input().split())
need_time = int(input())

time = H * 3600 + M * 60 + need_time * 60

hour = time // 3600
if hour >= 24:
    hour = hour - 24

print(hour, (time % 3600) // 60)
