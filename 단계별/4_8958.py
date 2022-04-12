N = int(input())

for i in range(N):
    res = input()

    score = 0
    total_score = []
    for j in res:
        if j == 'O':
            score += 1
        else:
            score = 0
        total_score.append(score)
    print(sum(total_score))
