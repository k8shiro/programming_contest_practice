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
    
    # defaultdictで保存
    # from collections import defaultdict
    # grid = defaultdict(lambda: defaultdict(int))

    cards = []
    h_list = set()  # 高さのリスト
    w_list = set()  # 幅のリスト

    for i in range(1, N+1):
        A, B = map(int, stdin.readline().split())
        cards.append((i, A, B))
        h_list.add(A)
        w_list.add(B)

    # グリッドを出力
    # print("========================")
    # for h, h_val in grid.items():
    #     for w, w_val in h_val.items():
    #         print(h, w, w_val)

    # ソート
    h_list = sorted(h_list)
    w_list = sorted(w_list)
    cards.sort(key=lambda x: x[0])  # 数値カードの順にソート

    h_list_index = {h: i for i, h in enumerate(h_list)}
    w_list_index = {w: i for i, w in enumerate(w_list)}
    for num, h, w in cards:
        h_index = h_list_index[h]
        w_index = w_list_index[w]
        print(h_index + 1, w_index + 1)





if __name__ == "__main__":
    main()


# たぶんTLE
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# from decimal import Decimal

# # メモ化
# from functools import lru_cache

# # 探索失敗用にINT_MAXを定義
# INT_MAX = 10**18

# # 10^9 + 7
# MOD = 10**9 + 7


# def main():
#     H, W, N = map(int, stdin.readline().split())
    
#     # 高さH、幅Wのグリッドを作成
#     grid = [[0] * W for _ in range(H)]
#     row = set() #0-indexedの行に数値カードが配置されているかを確認するためのセット 
#     col = set() #0-indexedの列に数値カードが配置されているかを確認するためのセット
    
#     for i in range(1, N+1):
#         A, B = map(int, stdin.readline().split())
#         grid[A-1][B-1] = i  # 1-indexedから0-indexedに変換して配置
#         row.add(A-1)
#         col.add(B-1)

#     # グリッドを出力
#     print("========================")
#     for r in grid:
#         print(" ".join(map(str, r)))

#     # 数値カードがない行を消す
#     new_grid = []
#     for i in range(H):
#         if i in row:
#             new_grid.append(grid[i])

#     # new_gridを出力
#     print("========================")
#     for r in new_grid:
#         print(" ".join(map(str, r)))

#     # グリッドを90度回転させる
#     transposed =[list(reversed(col)) for col in zip(*new_grid)]

#     # transposedを出力
#     print("========================")
#     for r in transposed:
#         print(" ".join(map(str, r)))

#     # 数値カードがない列を消す
#     new_grid = []
#     for i in range(len(transposed)):
#         if i in col:
#             new_grid.append(transposed[i])
#     # new_gridを出力
#     print("========================")
#     for r in new_grid:
#         print(" ".join(map(str, r)))

#     # グリッドを-90度回転させる
#     transposed = [list(col) for col in zip(*new_grid)][::-1]

#     # transposedを出力
#     print("========================")
#     for r in transposed:
#         print(" ".join(map(str, r)))

#     # カードの位置を確認
#     ans = []
#     for i in range(len(transposed)):
#         for j in range(len(transposed[i])):
#             if transposed[i][j] != 0:
#                 ans.append((transposed[i][j], i + 1, j + 1))
#     ans.sort()
#     for num, h, w in ans:
#         print(h, w)


# if __name__ == "__main__":
#     main()
