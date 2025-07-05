from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

from decimal import Decimal

# メモ化
from functools import lru_cache

# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18

# 10^9 + 7
MOD = 10**9 + 7


def main():
    T = int(stdin.readline().strip())

    case_list = []
    for _ in range(T):
        N = int(stdin.readline().strip())
        S = list(map(int, stdin.readline().strip().split()))
        case_list.append(S)
    
    #print("======")
    for S in case_list:  
        # print("S:", S)      
        start = S[0]
        end = S[-1]

        if start * 2 >= end:
            print(2)
            continue

        S = S[1:-1]
        S.sort()

        def check():
            ans= 2
            now = start
            next_domino = -1
            idx = 0
            while idx < len(S):
                if now * 2 >= S[idx]:
                    next_domino = S[idx]
                    idx += 1
                    if next_domino * 2 >= end:
                        ans += 1
                        print(ans)
                        return
                else:
                    if next_domino == -1:
                        print(-1)
                        return
                    else:
                        ans += 1
                        now = next_domino
                        next_domino = -1
                        
            if next_domino * 2 >= end:
                ans += 1
                print(ans)
            else:
                print(-1)
            return

        check()





if __name__ == "__main__":
    main()
