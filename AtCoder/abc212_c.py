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
    N, M = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))
    _A = [(a, 'A') for a in A]
    _B = [(b, 'B') for b in B]
    AB = _A + _B
    AB.sort()
    # print(AB)

    ans = INT_MAX
    for idx in range(1, N + M):
        if AB[idx][1] != AB[idx - 1][1]:
            ans = min(ans, AB[idx][0] - AB[idx - 1][0])
    print(ans)



if __name__ == "__main__":
    main()