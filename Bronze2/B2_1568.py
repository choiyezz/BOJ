N = int(input())
song = 1
count = 0
while N > 0:
    N -= song
    count += 1
    if song < N:
        song += 1
    else:
        song = 1
print(count)
