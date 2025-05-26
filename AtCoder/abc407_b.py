from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    X, Y = map(int, stdin.readline().split())

    ok_count = 0
    for dice_a in range(1, 7):
        for dice_b in range(1, 7):
            if dice_a + dice_b >= X or (dice_a - dice_b) ** 2 >= Y ** 2:
                ok_count += 1
    import decimal
    ANS = decimal.Decimal(ok_count) / decimal.Decimal(36)
    print(ANS)
            


    



if __name__ == "__main__":
    main()