from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


def main():
    X = int(stdin.readline())

    COUNT_KUKU = [0] * (9 * 9 + 1)
    SUM_KUKU = 0
    for i in range(1, 10):
        for j in range(1, 10):
            COUNT_KUKU[i * j] += 1
            SUM_KUKU += i * j 
    ANS = SUM_KUKU - COUNT_KUKU[X] * X
    print(ANS)
    


if __name__ == "__main__":
    main()