mylist = []
count = 0
for i in range(8):
    sublist = list(input())
    mylist.append(sublist)

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and mylist[i][j] == 'F':
            count += 1
        elif i % 2 != 0 and j % 2 != 0 and mylist[i][j] == 'F':
            count += 1
print(count)
