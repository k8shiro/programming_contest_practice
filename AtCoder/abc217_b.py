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

    AtCoder = set(['ABC', 'ARC', 'AGC', 'AHC'])
    AtCoder.remove(S1)
    AtCoder.remove(S2)
    AtCoder.remove(S3)
    print(AtCoder.pop())


 

if __name__ == "__main__":
    main()
