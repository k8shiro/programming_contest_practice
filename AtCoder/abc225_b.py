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
    graph = {i : [] for i in range(1, N+1)}
    for _ in range(N-1):
        a, b = map(int, stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    for node, next_nodes in graph.items():
        if len(next_nodes) == N-1:
            print("Yes")
            return
    print("No")






if __name__ == "__main__":
    main()
