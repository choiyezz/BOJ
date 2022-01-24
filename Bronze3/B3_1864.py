dic = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4,
       '>': 5, '&': 6, '%': 7, '/': -1}

while True:
    word = input()
    res = 0
    if word == '#':
        break
    word = word[::-1]

    for i in range(len(word)):
        res += dic[word[i]] * (8**i)
    print(res)

