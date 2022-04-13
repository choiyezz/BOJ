def d(n):
    n += sum(map(int, str(n)))
    return n


# 중복을 제거 하기 위한 필터 역할
Not_self_num = set()
for i in range(1, 10001):
    # 셀프 넘버가 아닌 수 추가
    Not_self_num.add(d(i))

# 셀프 넘버 출력 하기
for i in range(1, 10001):
    if i not in Not_self_num:
        print(i)
