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
            MIN_ROUTE.append((0, 0))
        elif n_idx == 1:
            MIN_ROUTE.append((A[0], -1))
        else:
            route_a = A[n_idx - 1] + MIN_ROUTE[n_idx - 1][0]
            route_b = B[n_idx - 2] + MIN_ROUTE[n_idx - 2][0]
            if route_a < route_b:
                MIN_ROUTE.append((route_a, -1))
            else:
                MIN_ROUTE.append((route_b, -2))

        n_idx += 1

    ANS_ROUTE = []
    n_idx = N - 1
    while n_idx > 0:
        ANS_ROUTE.append(n_idx)
        n_idx += MIN_ROUTE[n_idx][1]
    ANS_ROUTE.append(0)
    ANS_ROUTE.reverse()
    ANS_ROUTE = [x + 1 for x in ANS_ROUTE]
    print(len(ANS_ROUTE))
    print(' '.join(map(str, ANS_ROUTE)))


if __name__ == "__main__":
    main()