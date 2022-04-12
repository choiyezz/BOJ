remainder = []

for i in range(10):
    num = int(input())
    if num % 42 not in remainder:
        remainder.append(num % 42)
print(len(remainder))

"""
mylist = list(int(input()) for i in range(10))
remainder = list(0 for j in range(42))

for i in mylist:
    remainder[i % 42] += 1

count = 0
for i in remainder:
    if i >= 1:
        count += 1
print(count)
"""
