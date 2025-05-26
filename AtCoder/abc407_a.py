from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    A, B = map(int, stdin.readline().split())

    from decimal import Decimal
    div = Decimal(A) / Decimal(B)

    # 小数第一位を四捨五入(0.5なら1にする)
    div = round(div) 
    ANS = int(div)
    print(ANS)


    



if __name__ == "__main__":
    main()