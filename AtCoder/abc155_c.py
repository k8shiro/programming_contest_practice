

n = int(input())

from collections import defaultdict
ans = defaultdict(lambda: 0)

for _ in range(n):
    s = input()
    ans[s] += 1

max_value = max(ans.values())
max_keys = [k for k, v in ans.items() if v == max_value]
max_keys.sort()
for k in max_keys:
    print(k)