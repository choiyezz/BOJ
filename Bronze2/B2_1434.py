N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
i = j = 0

while i < N and j < M:
    if A[i] - B[j] < 0:
        i += 1
    else:
        A[i] = A[i] - B[j]
        j += 1
print(sum(A))

"""
print(sum(A) - sum(B))
"""
