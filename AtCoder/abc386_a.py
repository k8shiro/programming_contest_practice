from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    A, B, C, D = map(int, stdin.readline().split())
    CARDS = [A, B, C, D]
    CARDS = set(CARDS)

    if len(CARDS) == 2:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()