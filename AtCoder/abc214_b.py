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
    S, T = map(int, stdin.readline().split())
    
    count = 0
    for a in range(S + 1):
        for b in range(S - a + 1):
            if a + b > S:
                break
            for c in range(S - a - b + 1):
                if a * b * c <= T:
                    count += 1
                    
    print(count)
 

if __name__ == "__main__":
    main()
