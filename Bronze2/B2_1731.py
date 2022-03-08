N = int(input())
elem = []
for i in range(N):
    elem.append(int(input()))

if (elem[1] - elem[0]) == (elem[2] - elem[1]):
    print(elem[-1] + (elem[1] - elem[0]))
else:
    print(elem[-1] * (elem[1] // elem[0]))
