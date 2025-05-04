from sys import stdin

def main():
    N = int(stdin.readline())
    ANS_NUM = [0 for _ in range(10)]

    idx = -1
    while N > 0:
        ANS_NUM[idx] = N % 2
        N = N // 2
        idx -= 1

    ANS_STR = ''.join([str(i) for i in ANS_NUM])
    print(ANS_STR)
    return

if __name__ == "__main__":
    main()