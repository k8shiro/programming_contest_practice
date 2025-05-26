from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    H, W = map(int, stdin.readline().split())
    MEIRO = [['#'] * (W + 2)]
    for _ in range(H):
        S = list(stdin.readline().strip())
        MEIRO.append(['#'] + S + ['#'])
    MEIRO.append(['#'] * (W + 2))

    # スタート地点を見つける
    START = (-1, -1)
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if MEIRO[i][j] == 'S':
                START = (i, j)
                break
        if START != (-1, -1):
            break

    
    # 幅優先探索を開始
    # 探索済みの記録
    visited = [[[INT_MAX, INT_MAX] for _ in range(W + 2)] for _ in range(H + 2)]

    # 今のx座標、今のy座標、前回縦移動したか(bool)、移動回数
    from collections import deque
    pos = deque([(START[0], START[1], True, 0), (START[0], START[1], False, 0)])

    while pos:
        x, y, tate, count = pos.popleft()

        # すでに訪れた場所ならスキップ
        if visited[x][y][tate] <= count:
            continue
        visited[x][y][tate] = count

        # ゴールに到達した場合
        if MEIRO[x][y] == 'G':
            print(count)
            return

        if tate:
            # 前回縦移動した場合、横移動のみ可能
            if MEIRO[x-1][y] != '#':
                pos.append((x-1, y, False, count + 1))
            if MEIRO[x+1][y] != '#':
                pos.append((x+1, y, False, count + 1))
        else:
            # 前回横移動した場合、縦移動のみ可能
            if MEIRO[x][y-1] != '#':
                pos.append((x, y-1, True, count + 1))
            if MEIRO[x][y+1] != '#':
                pos.append((x, y+1, True, count + 1))
    
    # 探索失敗の場合
    print(-1)







if __name__ == "__main__":
    main()