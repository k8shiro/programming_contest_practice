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
    S1 = str(stdin.readline().strip())
    S2 = str(stdin.readline().strip())
    S3 = str(stdin.readline().strip())
    T = str(stdin.readline().strip())
    S = {
        '1': S1,
        '2': S2,
        '3': S3
    }

    ANS= ''
    for t in T:
        ANS += S[t]
    print(ANS)



 

if __name__ == "__main__":
    main()
