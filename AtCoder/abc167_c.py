from sys import stdin

n, m, x = map(int, stdin.readline().split())
a = []
for _ in range(n):
    _a = list(map(int, stdin.readline().split()))
    a.append(_a)

min_sum = float("inf")
for bit in range(2 ** n):
    #print(bin(bit))
    sum_a = [0] * m
    sum_c = 0
    for i in range(n):
        if (bit >> i) & 1 == 0:
            continue
        sum_c += a[i][0]
        for j in range(m):
            sum_a[j] += a[i][j+1]

    if min(sum_a) >= x:
        min_sum = min(min_sum, sum_c)

if min_sum == float("inf"):
    print(-1)
else:
    print(min_sum)

