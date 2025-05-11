from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    S = int(stdin.readline())
    if 200 <= S and S<=299:
        print("Success")
    else:
        print("Failure")
    

if __name__ == "__main__":
    main()