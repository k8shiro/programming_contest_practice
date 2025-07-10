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
    S = []
    for i in range(N):
        s = str(stdin.readline().strip())
        S.append(s)

    set_S = set()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            _s = S[i] + S[j]
            set_S.add(_s)

    print(len(set_S))
            


if __name__ == "__main__":
    main()
