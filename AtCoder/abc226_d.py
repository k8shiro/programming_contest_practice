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

    zahyo = dict()
    for node in range(N):
        node += 1 # 1-indexed
        x, y = map(int, stdin.readline().strip().split())
        zahyo[node] = (x, y)

    maho = set()
    for start in range(1, N + 1):
        for end in range(1, N + 1):
            if start == end:
                continue
            start_x, start_y = zahyo[start]
            end_x, end_y = zahyo[end]
            maho_x = end_x - start_x
            maho_y = end_y - start_y 
            gcd_value = gcd_multiple(maho_x, maho_y)
            if gcd_value != 0:
                maho_x //= gcd_value
                maho_y //= gcd_value
            maho.add((maho_x, maho_y))
    print(len(maho))

            

import math
from functools import reduce

def gcd_multiple(*numbers):
    return reduce(math.gcd, numbers)



if __name__ == "__main__":
    main()
