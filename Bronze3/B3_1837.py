# 소수란 1과 자기 자신을 제외한 자연수로 나누어 떨어지지 않는 자연수
P, K = map(int, input().split())
flag = True
for i in range(2, K):
    if P % i == 0:
        print("BAD", i)
        flag = False
        break
if flag is True:
    print("GOOD")

