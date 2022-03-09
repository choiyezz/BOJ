N, C = map(int, input().split())
time = [0] * (C+1)
count = 0
for i in range(N):
    fire = int(input())
    for j in range(fire, C+1, fire):
        if time[j] == 0:
            time[j] = 1
            count += 1
print(count)


