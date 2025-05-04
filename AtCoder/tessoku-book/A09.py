from sys import stdin

def main():
    H, W, N = map(int, stdin.readline().split())

    # 二次元の0で埋められたリストを作成
    # 行ごとに左セルからの増減を示す
    YUKI = [[0] * (W+2) for _ in range(H)]

    for _ in range(N):
        A, B, C, D = map(int, stdin.readline().split())
        for i in range(A-1, C):
            YUKI[i][B] += 1
            YUKI[i][D+1] -= 1

    HW = [[0] * (W+1) for _ in range(H)]
    for h in range(H):
        for w in range(1, W+1):
            HW[h][w] = HW[h][w-1] + YUKI[h][w]

    for h in range(H):
        OUTPUT = ' '.join(map(str, HW[h][1:W+1]))
        print(OUTPUT)

if __name__ == "__main__":
    main()