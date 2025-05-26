from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    S = str(stdin.readline().rstrip())
    S = S.split('x')
    print(int(S[0])*int(S[1]))



if __name__ == "__main__":
    main()