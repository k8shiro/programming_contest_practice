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

MOD = 998244353
def main():
    N = int(stdin.readline().strip())

    term1 = ((N * ((N + 1) % MOD)) % MOD * pow(2, MOD - 2, MOD)) % MOD

    sum_f = 0
    i = 1
    while i <= N:
        val = N // i
        j = N // val
        count = j - i + 1
        count_mod = count % MOD
        val_mod = val % MOD
        term = (count_mod * val_mod) % MOD
        sum_f = (sum_f + term) % MOD
        i = j + 1
    ans = (term1 - sum_f + MOD) % MOD

    print(ans)

            


if __name__ == "__main__":
    main()
