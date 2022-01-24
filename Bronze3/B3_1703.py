while True:
    mylist = list(map(int, input().split()))
    if mylist[0] == 0:
        break
    else:
        res = 1
        for i in range(1, len(mylist)):
            if i % 2 != 0:
                res *= mylist[i]
            else:
                res -= mylist[i]
        print(res)

"""
참고용으로 가져옴
while True:
    tree = list(map(int, input().split()))
    leaf = 1
    if tree[0] == 0:
        break
    for i in range(1, len(tree), 2):
        leaf = leaf * tree[i] - tree[i+1]
    print(leaf)
"""