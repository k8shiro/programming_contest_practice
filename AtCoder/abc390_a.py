from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    A = list(map(int, stdin.readline().split()))
    
    # Aをソート
    A_SORTED = sorted(A)
    A_SORTED = '_'.join(map(str, A_SORTED))

    for idx in range(1, len(A)):
        _A = A[:idx-1] + [A[idx]] + [A[idx-1]] + A[idx+1:]
        _A = '_'.join(map(str, _A))
        if A_SORTED == _A:
            print("Yes")
            return
    print("No")




    

if __name__ == "__main__":
    main()