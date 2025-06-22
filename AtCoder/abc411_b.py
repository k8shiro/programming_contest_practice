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
    D = list(map(int, stdin.readline().strip().split()))

    for i in range(1, N):
        ANS = []
        start = 0
        for d in D[i-1:]:
            start += d
            ANS.append(start)
        print(*ANS)







if __name__ == "__main__":
    main()
