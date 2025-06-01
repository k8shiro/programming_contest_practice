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

    # from decimal import Decimal, getcontext
    # getcontext().prec = 2000   # 精度を設定 1000では成功しない
    # N = Decimal(N)
    # log2N = N.log10() / Decimal(2).log10()
    # print(int(log2N))

 
    from mpmath import mp
    mp.dps = 100
    log2n_mpmath = mp.log(N, 2)
    log2n_mpmath = int(log2n_mpmath)
    print(log2n_mpmath)

if __name__ == "__main__":
    main()
