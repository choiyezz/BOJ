x, y, w, h = map(int, input().split())
mylist = [x, y, w-x, h-y]
print(min(mylist))



