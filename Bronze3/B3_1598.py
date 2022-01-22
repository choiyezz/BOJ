num1, num2 = map(int, input().split())
num1 -= 1
num2 -= 1
a = num1 // 4
b = num1 % 4
c = num2 // 4
d = num2 % 4
print(abs(a-c)+abs(b-d))


