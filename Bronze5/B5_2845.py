people, place = map(int, input().split())
news = list(map(int, input().split()))

for i in news:
    print(i - (people * place), end=' ')
