mo = ['a', 'e', 'i', 'o', 'u']

while True:
    a = input().lower()
    count = 0
    if a == '#':
        break
    else:
        mylist = list(a)
        for i in range(len(mylist)):
            if mylist[i] in mo:
                count += 1
    print(count)



