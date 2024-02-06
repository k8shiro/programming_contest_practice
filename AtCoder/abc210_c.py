from sys import stdin
n, k = map(int, stdin.readline().split())
c = map(int, stdin.readline().split())
c = list(c)

from collections import defaultdict
counter = defaultdict(lambda: 0)

for i in range(k):
    counter[c[i]] += 1

max_value = len(counter.keys())
for i in range(k, n):
    counter[c[i]] += 1
    counter[c[i-k]] -= 1
    if counter[c[i-k]] == 0:
        del counter[c[i-k]]
    max_value = max(max_value, len(counter.keys()))

print(max_value)