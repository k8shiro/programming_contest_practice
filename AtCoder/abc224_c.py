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
    points = []
    for _ in range(N):
        X, Y = map(int, stdin.readline().strip().split())
        points.append((X, Y))

    from itertools import combinations
    count = 0
    for p1, p2, p3 in combinations(points, 3):
        area = triangle_area(p1, p2, p3)
        if area > 0:
            count += 1

    print(count)


# 3点の座標から三角形の面積を計算する関数
def triangle_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

if __name__ == "__main__":
    main()
