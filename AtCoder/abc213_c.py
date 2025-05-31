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
    H, W, N = map(int, stdin.readline().split())
    
    # 高さH、幅Wのグリッドを作成
    grid = [[0] * W for _ in range(H)]
    row = set() #0-indexedの行に数値カードが配置されているかを確認するためのセット 
    col = set() #0-indexedの列に数値カードが配置されているかを確認するためのセット
    
    for i in range(1, N+1):
        A, B = map(int, stdin.readline().split())
        grid[A-1][B-1] = i  # 1-indexedから0-indexedに変換して配置
        row.add(A-1)
        col.add(B-1)

    # グリッドを出力
    print("========================")
    for r in grid:
        print(" ".join(map(str, r)))

    # 数値カードがない行を消す
    new_grid = []
    for i in range(H):
        if i in row:
            new_grid.append(grid[i])

    # new_gridを出力
    print("========================")
    for r in new_grid:
        print(" ".join(map(str, r)))

    transposed = list(map(list, zip(*new_grid)))  # グリッドを転置
    # transposedを出力
    print("========================")
    for r in transposed:
        print(" ".join(map(str, r)))


if __name__ == "__main__":
    main()
