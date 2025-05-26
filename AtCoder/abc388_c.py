from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))

    ANS = 0
    import bisect
    for a in A:
        idx = bisect.bisect_left(A, a*2)
        # print(idx)
        ANS += N - idx
    print(ANS)




if __name__ == "__main__":
    main()
