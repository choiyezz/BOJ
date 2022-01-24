num = int(input())
start = 5
var = 7
for i in range(1, num):
    start += var
    var += 3
print(start % 45678)
