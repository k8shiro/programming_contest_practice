n = int(input())

s_list = []

for _ in range(n):
    s = list(input())
    s.sort()
    s = ''.join(s)
    s_list.append(s)

from collections import defaultdict
counter = defaultdict(lambda: 0)

for s in s_list:
    counter[s] += 1

ans = 0
for v in counter.values():
    nC2 = v * (v - 1) // 2
    ans += nC2

print(ans)
