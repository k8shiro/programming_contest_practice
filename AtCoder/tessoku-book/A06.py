from sys import stdin

def main():
    N, Q = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    SUM_A = [0] # idx日目の累積和
    SUM = 0
    for a in A:
        SUM += a
        SUM_A.append(SUM)

    for _ in range(Q):
        L, R = map(int, stdin.readline().split())
        ANS = SUM_A[R] - SUM_A[L-1]
        print(ANS)
    return


if __name__ == "__main__":
    main()
