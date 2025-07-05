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
    S = str(stdin.readline().strip())
    T = str(stdin.readline().strip())

    chrs = set()
    for idx in range(len(S)):
        if idx == 0:
            continue
        if idx == 1:
            continue

        # 大文字か判定
        if S[idx].isupper():
            chrs.add(S[idx-1])

    T = set(T)

    # charsがTに含まれているか判定
    for c in chrs:
        if c not in T:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
