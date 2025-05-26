from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


def main():
    N, D = map(int, stdin.readline().split())
    HEAVY = [0] * D
    for _ in range(N):
        T, L = map(int, stdin.readline().split())
        for d in range(D):
            HEAVY[d] = max(HEAVY[d], T * (L + d + 1))
    for h in HEAVY:
        print(h)




if __name__ == "__main__":
    main()
