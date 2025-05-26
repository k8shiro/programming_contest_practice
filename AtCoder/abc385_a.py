from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    A, B, C = map(int, stdin.readline().split())
    ABC = [A, B, C]
    ABC.sort()

    A, B, C = ABC
    if A == B == C:
        print("Yes")
    elif A + B == C:
        print("Yes")
    else:
        print("No")





if __name__ == "__main__":
    main()
