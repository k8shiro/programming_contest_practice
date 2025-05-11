from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(stdin.readline())
    status = 'logout'
    error_count = 0
    for _ in range(N):
        S = stdin.readline().rstrip()
        if S == 'logout':
            status = S
        elif S == 'login':
            status = S
        elif S == 'public':
            pass
        elif S == 'private':
            if status == 'login':
                pass
            else:
                error_count += 1
    print(error_count)

    

if __name__ == "__main__":
    main()