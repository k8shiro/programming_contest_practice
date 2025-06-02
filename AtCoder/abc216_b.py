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
    names = set()
    same_flag = False
    for _ in range(N):
        ST = str(stdin.readline().strip())
        if not ST in names:
            names.add(ST)
        else:
            same_flag = True

    if same_flag:
        print("Yes")
    else:
        print("No")




 

if __name__ == "__main__":
    main()
