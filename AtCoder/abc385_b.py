from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    H, W, X, Y = map(int, stdin.readline().split())
    S = []
    for _ in range(H):
        s = list(stdin.readline().rstrip())
        S.append(s)
    T = str(stdin.readline().rstrip())

    santa_pos = (X-1, Y-1) # サンタの位置
    home_count = 0
    for t in T:
        x, y = santa_pos
        if t == 'U':
            next_pos = (x - 1, y)
        if t == 'D':
            next_pos = (x + 1, y)
        if t == 'L':
            next_pos = (x, y - 1)
        if t == 'R':
            next_pos = (x, y + 1)
        if S[next_pos[0]][next_pos[1]] == '#':
            continue
        elif S[next_pos[0]][next_pos[1]] == '@':
            home_count += 1
            S[next_pos[0]][next_pos[1]] = '.'
            santa_pos = next_pos
        else:
            santa_pos = next_pos
    print(santa_pos[0]+1, santa_pos[1]+1, home_count)


if __name__ == "__main__":
    main()
