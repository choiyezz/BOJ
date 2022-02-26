N = map(int, input().split())
people = list(map(int, input().split()))
seat = [0] * 100
count = 0
for i in people:
    if seat[i-1] == 0:
        seat[i-1] += 1
    else:
        count += 1
print(count)


