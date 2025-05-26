from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


def main():
    A, B = map(int, stdin.readline().split())
    ANS = (A + B) ** 2
    print(ANS)


if __name__ == "__main__":
    main()