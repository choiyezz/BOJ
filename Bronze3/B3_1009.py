case = int(input())
for i in range(case):
    a, b = map(int, input().split())
    aa = a % 10
    if aa == 0: # 패턴1
        print(10)
    elif aa in [1, 5, 6]:
        print(aa)
    elif aa in [4, 9]:  # 패턴2
        bb = b % 2
        # 지수가 1이면 aa ** 1 이기 때문에 aa만 출력
        if bb == 1:
            print(aa)
        else:
            print((aa*aa) % 10)
    else:
        bb = b % 4
        # bb 가 0 이면 aa ** 0 이 되기 때문에 **4 로 처리 한다.
        if bb == 0:
            print((aa**4) % 10)
        else:
            print((aa**bb) % 10)
