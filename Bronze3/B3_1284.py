while True:
    num = input()
    # 호수판의 오른쪽, 왼쪽 경계에서 발생하는 여백 2cm
    res = 2
    if num == '0':
        break
    else:
        for i in num:
            if i == '0':
                res += 4
            elif i == '1':
                res += 2
            else:
                res += 3
            # 숫자 사이의 여백 1cm
            res += 1
        # 마지막 숫자 뒤 여백 1cm 가 더해져 경계면과 숫자 사이의 여백이 2cm 가 되기때문에 1cm 를 빼준다
        print(res-1)
