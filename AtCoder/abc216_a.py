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
    XY = str(stdin.readline().strip())

    # '.'で分割して、xとyを取得
    x, y = XY.split('.')
    # xを整数に変換
    x = int(x)
    # yを整数に変換
    y = int(y)
    
    if 0 <= y <= 2:
        print(f"{x}-")
    elif 3 <= y <= 6:
        print(f"{x}")
    elif 7 <= y <= 9:
        print(f"{x}+")


 

if __name__ == "__main__":
    main()
