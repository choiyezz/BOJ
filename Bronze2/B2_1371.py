import sys
a = sys.stdin.read()
res = [0]*26

for i in a:
    if i.islower():
        res[ord(i)-97] += 1
for i in range(len(res)):
    if res[i] == max(res):
        print(chr(i+97), end='')
