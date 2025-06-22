from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

from decimal import Decimal

# メモ化
from functools import lru_cache

# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18

# 10^9 + 7
MOD = 10**9 + 7


def main():
    N = int(stdin.readline().strip())
    A = []
    for _ in range(N):
        a = list(map(int, stdin.readline().strip().split()))
        A.append(a)


    waza = dict()
    for node, a_list in enumerate(A):
        node += 1  # 1-indexedにする
        t = a_list[0]
        k = a_list[1]
        waza[node] = {
            'time': t,
            'izon': a_list[2:]
        }


    from collections import deque
    queue = deque(waza[N]['izon'])
    visited = set()
    visited.add(N)

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        for next_node in waza[current]['izon']:
            if next_node not in visited:
                queue.append(next_node)

    ans = 0
    for node in visited:
        ans += waza[node]['time']
    
    # print("============")
    # print(waza)
    # print(visited)
    print(ans)

    

            





if __name__ == "__main__":
    main()
