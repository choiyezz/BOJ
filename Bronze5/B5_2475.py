# 1번
number = list(map(int, input().split()))
for i in range(len(number)):
    number[i] = number[i] ** 2

print(sum(number) % 10)

# 2번
res = 0
for i in list(map(int, input().split())):
    res += i ** 2
print(res % 10)
