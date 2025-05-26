from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    S = str(stdin.readline().strip())

    # 最初に見つけた"00"を"z"に置き換える
    while "00" in S:
        S = S.replace("00", "z", 1)
    
    print(len(S))

if __name__ == "__main__":
    main()