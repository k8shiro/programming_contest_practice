from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)
BOX = []
def main():
    H, W = map(int, stdin.readline().split())
    for _ in range(H):
        S = list(stdin.readline().rstrip())
        BOX.append(S)

    min_h = 9999
    min_w = 9999
    max_h = -1
    max_w = -1

    for h in range(H):
        for w in range(W):
            if BOX[h][w] == "#":
                min_h = min(min_h, h)
                min_w = min(min_w, w)
                max_h = max(max_h, h)
                max_w = max(max_w, w)

    for h in range(min_h, max_h + 1):
        for w in range(min_w, max_w + 1):
            if BOX[h][w] == ".":
                print("No")
                return
    print("Yes")



if __name__ == "__main__":
    main()