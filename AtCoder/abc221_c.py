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
    N = str(stdin.readline().strip())
    N_LIST = list(N)
    N_LIST = [int(n) for n in N_LIST]

    N_GROUPS = assign_to_two_boxes(N_LIST)
    # print(N_GROUPS)

    ANS = 0
    for group1, group2 in N_GROUPS:
        if not group1 or not group2:
            continue
        group1.sort(reverse=True)
        group2.sort(reverse=True)
        
        if group1[0] == 0 or group2[0] == 0:
            continue

        num1 = int(''.join(map(str, group1)))
        num2 = int(''.join(map(str, group2)))
        ANS = max(ANS, num1 * num2)

    print(ANS)

from itertools import product

def assign_to_two_boxes(arr):
    n = len(arr)
    result = []

    # 各要素に「0（箱A）」または「1（箱B）」の割り当て方を全通り列挙
    for bits in product((0, 1), repeat=n):
        box1 = [arr[i] for i in range(n) if bits[i] == 0]
        box2 = [arr[i] for i in range(n) if bits[i] == 1]
        result.append((box1, box2))

    return result


if __name__ == "__main__":
    main()
