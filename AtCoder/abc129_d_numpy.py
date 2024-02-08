
from sys import stdin
import numpy as np

def main():
    h, w = map(int, stdin.readline().split())

    s = np.array([list(stdin.readline().strip()) for _ in range(h)])
    s = np.where(s == '#', 0, 1)

    s_l = np.zeros((h, w), dtype=int)
    s_r = np.zeros((h, w), dtype=int)
    s_t = np.zeros((h, w), dtype=int)
    s_u = np.zeros((h, w), dtype=int)

    # 左方向に連続するドットの数を計算
    for i in range(w):
        if i == 0:
            s_l[:, i] = 1 * s[:, i]
        else:
            s_l[:, i] = (s_l[:, i-1]  + 1) * s[:, i]
        

    # 右方向に連続するドットの数を計算
    for i in reversed(range(w)):
        if i == w-1:
            s_r[:, i] = 1 * s[:, i]
        else:
            s_r[:, i] = (s_r[:, i+1]  + 1) * s[:, i]

    # 上方向に連続するドットの数を計算
    for i in range(h):
        if i == 0:
            s_t[i] = 1 * s[i]
        else:
            s_t[i] = (s_t[i-1] + 1) * s[i]

    # 下方向に連続するドットの数を計算
    for i in reversed(range(h)):
        if i == h-1:
            s_u[i] = 1 * s[i]
        else:
            s_u[i] = (s_u[i+1] + 1) * s[i]

    ans = np.max(s_l + s_r + s_t + s_u - 3)
    print(ans)

main()

