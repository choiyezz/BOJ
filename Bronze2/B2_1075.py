N = int(input())
F = int(input())
num = N - (N % 100)
res1 = num // F
res2 = res1 * F
if res2 >= num:
    print('%02d' % (res2 % 100))
else:
    print('%02d' % ((res2+F) % 100))

"""
N = input()
F = int(input())

temp = int(N[:-2] + '00')
while True:
    if temp % F == 0:
        break
    temp += 1
print(str(temp)[-2:])
"""