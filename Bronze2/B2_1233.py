S1, S2, S3 = map(int, input().split())
mylist = [0] * (S1 + S2 + S3 + 1)

for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            mylist[i+j+k] += 1

max_sum = mylist[0]
idx = 0
for i in range(S1 + S2 + S3 + 1):
    if max_sum < mylist[i]:
        max_sum = mylist[i]
        idx = i
print(idx)






