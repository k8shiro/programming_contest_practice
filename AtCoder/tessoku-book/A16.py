from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))

    n_idx = 0
    MIN_ROUTE = []
    while n_idx < N:
        if n_idx == 0:
            MIN_ROUTE.append(0)
        elif n_idx == 1:
            MIN_ROUTE.append(A[0])
        else:
            route_a = A[n_idx - 1] + MIN_ROUTE[n_idx - 1]
            route_b = B[n_idx - 2] + MIN_ROUTE[n_idx - 2]
            MIN_ROUTE.append(min(route_a, route_b))

        n_idx += 1
    ANS = MIN_ROUTE[-1]
    print(ANS)


if __name__ == "__main__":
    main()