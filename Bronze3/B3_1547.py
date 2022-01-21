cup = [1, 0, 0]
num = int(input())
for i in range(num):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    cup[x], cup[y] = cup[y], cup[x]
print(cup.index(1) + 1)

