a = [0] * 26
b = a[:]
res = 0

for i in input():
    a[ord(i)-97] += 1
for i in input():
    b[ord(i)-97] += 1
for i in range(26):
    res += abs(a[i]-b[i])
print(res)
