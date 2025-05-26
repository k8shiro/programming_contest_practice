from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    N = int(stdin.readline().strip())
    
    if N == 1:
        print(1)
        print(1)
        return
    if N % 2 == 0:
        print(N // 2)
        ANS = [i * 2 for i in range(1, N // 2 + 1)]
        print(" ".join(map(str, ANS)))
        return
    if N % 2 == 1:
        print((N - 1) // 2)
        ANS = [i * 2 for i in range(1, (N - 1) // 2 + 1)]
        print(" ".join(map(str, ANS)))
        return


if __name__ == "__main__":
    main()
