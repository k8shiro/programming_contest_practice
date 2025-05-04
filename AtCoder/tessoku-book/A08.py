from sys import stdin

def main():
    H, W = map(int, stdin.readline().split())
    X = []
    for _ in range(H):
        x = list(map(int, stdin.readline().split()))
        X.append(x)

    _X = []
    for x in X:
        _x = [0]
        for v in x:
            _x.append(_x[-1] + v)
        _X.append(_x)

    Q = int(stdin.readline())
    for _ in range(Q):
        A, B, C, D = map(int, stdin.readline().split())
        ANS = 0
        for i in range(A - 1, C):
            ANS += _X[i][D] - _X[i][B - 1]
        print(ANS)

if __name__ == "__main__":
    main()