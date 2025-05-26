from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    N = int(stdin.readline().strip())
    H = list(map(int, stdin.readline().split()))


    ANS = 1
    for dist in range(1, N):
        for head in range(dist):
            head_height = H[head]
            # print(H[head::dist])
            count = 0
            _height = H[head::dist][0]
            for height in H[head::dist]:
                if _height == height:
                    count += 1
                    ANS = max(ANS, count)
                else:
                    _height = height
                    count = 1
    print(ANS)
                



if __name__ == "__main__":
    main()
