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

    S = []
    T = []

    replace_map = {'.': 0, '#': 1}
    for _ in range(N):
        s = list(stdin.readline().strip())
        s = [replace_map[char] for char in s]
        S.append(s)
    for _ in range(N):
        t = list(stdin.readline().strip())
        t = [replace_map[char] for char in t]
        T.append(t)

    # Sの図形の角を探す
    l_w = N - 1 # 左端の列
    r_w = 0 # 右端の列
    t_h = N - 1 # 上端の行
    b_h = 0 # 下端の行

    for h in range(N):
        for w in range(N):
            if S[h][w] == 1:
                l_w = min(l_w, w)
                r_w = max(r_w, w)
                t_h = min(t_h, h)
                b_h = max(b_h, h)
    S = [row[l_w:r_w + 1] for row in S[t_h:b_h + 1]]

    # Tの図形の角を探す
    l_w = N - 1 # 左端の列
    r_w = 0 # 右端の列
    t_h = N - 1 # 上端の行
    b_h = 0 # 下端の行
    for h in range(N):
        for w in range(N):
            if T[h][w] == 1:
                l_w = min(l_w, w)
                r_w = max(r_w, w)
                t_h = min(t_h, h)
                b_h = max(b_h, h)
    T = [row[l_w:r_w + 1] for row in T[t_h:b_h + 1]]

    # SとTをprint
    # for row in S:
    #     print(*row)
    # print("----------")
    # for row in T:
    #     print(*row)


    # 90度回転させる関数
    def rotate_90(matrix):
        rotated = [list(reversed(col)) for col in zip(*matrix)]
        return rotated

    # 比較
    if S == T:
        print("Yes")
        return
    
    # 90度回転させて比較
    S = rotate_90(S)
    if S == T:
        print("Yes")
        return

    # 180度回転させて比較
    S = rotate_90(S)
    if S == T:
        print("Yes")
        return

    # 270度回転させて比較
    S = rotate_90(S)
    if S == T:
        print("Yes")
        return

    print("No")
    return


if __name__ == "__main__":
    main()
