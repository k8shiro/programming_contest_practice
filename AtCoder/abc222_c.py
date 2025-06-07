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
    N, M = map(int, stdin.readline().strip().split())

    from sortedcontainers import SortedList
    A = SortedList()
    
    point = -100
    for i in range(2*N):
        a = str(stdin.readline().strip())
        point += 0.0001
        A.add((point, a, i+1))


    for r in range(M):
        new_A = SortedList()

        for k in range(N):
            a1 = A[2*k]
            a2 = A[2*k+1]

            if a1[1][r] == 'G' and a2[1][r] == 'C':
                new_A.add((a1[0] - 1, a1[1], a1[2]))
                new_A.add((a2[0], a2[1], a2[2]))
                continue
            if a1[1][r] == 'C' and a2[1][r] == 'G':
                new_A.add((a1[0], a1[1], a1[2]))
                new_A.add((a2[0] - 1, a2[1], a2[2]))
                continue
            
            if a1[1][r] == 'C' and a2[1][r] == 'P':
                new_A.add((a1[0] - 1, a1[1], a1[2]))
                new_A.add((a2[0], a2[1], a2[2]))
                continue
            if a1[1][r] == 'P' and a2[1][r] == 'C':
                new_A.add((a1[0], a1[1], a1[2]))
                new_A.add((a2[0] - 1, a2[1], a2[2]))
                continue

            if a1[1][r] == 'P' and a2[1][r] == 'G':
                new_A.add((a1[0] - 1, a1[1], a1[2]))
                new_A.add((a2[0], a2[1], a2[2]))
                continue
            if a1[1][r] == 'G' and a2[1][r] == 'P':
                new_A.add((a1[0], a1[1], a1[2]))
                new_A.add((a2[0] - 1, a2[1], a2[2]))
                continue

            new_A.add((a1[0], a1[1], a1[2]))
            new_A.add((a2[0], a2[1], a2[2]))

            

        A = new_A
        #print(A)

    for a in A:
        print(a[2])




if __name__ == "__main__":
    main()
