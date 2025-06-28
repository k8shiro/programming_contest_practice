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
    S = str(stdin.readline().strip())
    K = int(stdin.readline().strip())


    # 各文字種ごとの出現数カウンタ
    char_counts = [0] * 3  # 0: K, 1: E, 2: Y

    # 各文字の出現位置の状態（出現時点での[K, E, Y]の個数）を記録
    char_history = [[] for _ in range(3)]

    for idx, ch in enumerate(S):
        if ch == "K":
            char_history[0].append(tuple(char_counts))
            char_counts[0] += 1
        elif ch == "E":
            char_history[1].append(tuple(char_counts))
            char_counts[1] += 1
        else:  # ch == "Y"
            char_history[2].append(tuple(char_counts))
            char_counts[2] += 1

    from collections import defaultdict
    dp = [defaultdict(int) for _ in range(len(S)+1)]
    dp[0][(0, 0, 0, 0)] = 1

    for i in range(len(S)):
        for k, e, y, swap_count in dp[i].keys():
            current_ways = dp[i][(k, e, y, swap_count)]

            if k < char_counts[0]:
                k_pos = char_history[0][k]
                k_swaps = max(e - k_pos[1], 0) + max(y - k_pos[2], 0) # 余計なEYの出現数
                dp[i + 1][(k + 1, e, y, swap_count + k_swaps)] += current_ways
                    
            if e < char_counts[1]:
                e_pos = char_history[1][e]
                e_swaps = max(k - e_pos[0], 0) + max(y - e_pos[2], 0)
                dp[i + 1][(k, e + 1, y, swap_count + e_swaps)] += current_ways

            if y < char_counts[2]:
                y_pos = char_history[2][y]
                y_swaps = max(k - y_pos[0], 0) + max(e - y_pos[1], 0)
                dp[i + 1][(k, e, y + 1, swap_count + y_swaps)] += current_ways
                   
            
    answer = 0
    for k, e, y, swap_count in dp[len(S)].keys():
        if swap_count <= K:
            answer += dp[len(S)][(k, e, y, swap_count)]
    print(answer)

if __name__ == "__main__":
    main()

# def main():
#     S = str(stdin.readline().strip())
#     K = int(stdin.readline().strip())

#     count = {
#         'K': 0,
#         'E': 0,
#         'Y': 0
#     }

#     for c in S:
#         if c == 'K':
#             count['K'] += 1
#         elif c == 'E':
#             count['E'] += 1
#         elif c == 'Y':
#             count['Y'] += 1

#     paterns = gen_str(count['K'], count['E'], count['Y'], '')
#     # for s in paterns:
#     #     print(s)

#     ans = 0
#     for goal in paterns:
#         count = check(S, goal)
#         if count <= K:
#             ans += 1

#     print(ans)



# def gen_str(k, e, y, s):
#     if k == 0 and e == 0 and y == 0:
#         return [s]

#     result = []
#     if k > 0:
#         result += gen_str(k - 1, e, y, s + 'K')
#     if e > 0:
#         result += gen_str(k, e - 1, y, s + 'E')
#     if y > 0:
#         result += gen_str(k, e, y - 1, s + 'Y')

#     return result

# def check(s, goal):
#     s = list(s)
#     count = 0
#     for idx in range(len(s)):
#         # idx以上の文字でgoal[idx]と同じ文字を探す
#         for j in range(idx, len(s)):
#             if s[j] == goal[idx]:
#                 while j > idx:
#                     count += 1
#                     s[j], s[j - 1] = s[j - 1], s[j]
#                     j -= 1
#                 break
#     return count


# if __name__ == "__main__":
#     main()
