from collections import Counter
num = int(input())
mylist = []
for i in range(num):
    name = input()
    mylist.append(name[0])

ans = []
count = Counter(mylist)
for i in count:
    if count[i] >= 5:
        ans.append(i)
ans.sort()
if not ans:
    print("PREDAJA")
else:
    print(''.join(ans))

print(Counter(mylist))  # Counter({'k': 7, 'b': 6, 's': 2, 'p': 2, 'h': 1})
# '구분자'.join(리스트) : 리스트의 값과 값 사이에 구분자를 넣어 하나의 문자열로 합쳐서 반환
