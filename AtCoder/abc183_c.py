
from sys import stdin

n, k = map(int, stdin.readline().split())

t = []
for _ in range(n):
    _t = list(map(int, stdin.readline().split()))
    t.append(_t)

import sys
sys.setrecursionlimit(10 ** 6) # 再帰上限を増やす
def travel(start, cost, visited: set) -> int:
    #print(start, cost, visited)
    if len(visited) == n:
        cost += t[start][0]
        if cost == k:
            return 1
        else:
            return 0

    cnt = 0
    for goal, dist in enumerate(t[start]):
        if goal in visited:
            continue
        cnt += travel(goal, cost + dist, visited | {goal})
    
    return cnt

cnt = travel(0, 0, {0})
print(cnt)







