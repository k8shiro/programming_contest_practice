from sys import stdin

def main():
    N, K = map(int, stdin.readline().split())

    ANS = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i + j < K and i + j + N >= K:
                ANS += 1
    print(ANS)
    return


if __name__ == "__main__":
    main()
