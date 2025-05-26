from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    X = int(stdin.readline())
    num = 1
    while True:
        # print(X, num)
        if X // num == 1:
            print(num)
            return
        X = X // num
        num += 1
        


if __name__ == "__main__":
    main()