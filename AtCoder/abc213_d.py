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


VISITED = set()
from collections import defaultdict
PATHS = defaultdict(list)
ANS = []
def main():
    global VISITED, PATHS, ANS
    N = int(stdin.readline().strip())

    for _ in range(N-1):
        A, B = map(int, stdin.readline().split())
        PATHS[A].append(B)
        PATHS[B].append(A)

    for key in PATHS:
        PATHS[key].sort()

    # for key in PATHS:
    #     print(key, PATHS[key])

    # 深さ優先探索を開始
    dfs(1)
    # 結果を出力
    print(*ANS)


def dfs(now):
    global VISITED, PATHS, ANS
    VISITED.add(now)
    ANS.append(now)

    for next_node in PATHS[now]:
        if next_node not in VISITED:
            dfs(next_node)
            ANS.append(now)

if __name__ == "__main__":
    main()
