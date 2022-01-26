K, L = map(int, input().split())
flag = True
for i in range(2, L):
    if K % i == 0:
        print("BAD", i)
        flag = False
        break
if flag is True:
    print("GOOD")

