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

    points = set()
    for _ in range(N):
        x, y = map(int, stdin.readline().strip().split())
        points.add((x, y))

    count = 0
    from itertools import combinations
    for (x1, y1), (x2, y2) in combinations(points, 2):
        if x1 == x2 or y1 == y2:
            continue
        if ((x1, y2) in points) and ((x2, y1) in points):
            count += 1
    print(count // 2)




if __name__ == "__main__":
    main()
