from sys import stdin
A, B = stdin.readline().split()
A = list(map(int, A))
B = list(map(int, B))
print(sum(A) * sum(B))
