from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

mod = 10**9

from collections import deque
def main():
    N, K = map(int, stdin.readline().split())
    S = stdin.readline().rstrip()

    S2 = [S[0]]
    # 'o'の隣の'?'を'.'に変換
    for idx, s in enumerate(S):
        if idx == 0:
            continue
        if s == '?' and S[idx-1] == 'o':
            S2.append('.')
        elif s == '?' and idx+1 < N and S[idx+1] == 'o':
            S2.append('.')
        else:
            S2.append(s)

    # 'o'を数える
    conunt_o = 0
    for s in S2:
        if s == 'o':
            conunt_o += 1
        else:
            continue

    # conut_o == Kの時は'?'を'.'に変換してreturn
    if conunt_o == K:
        ANS = ''
        for s in S2:
            if s == '?':
                ANS += '.'
            else:
                ANS += s
        print(ANS)
        return

    # 連続した'?'
    import re
    block_q = re.findall(r'\?+', ''.join(S2))

    # '?'の数を数える
    block_q_count = []
    for b in block_q:
        block_q_count.append(len(b))
    

    # 'o'の最大値を出す
    import math
    max_o = conunt_o
    for len_b in block_q_count:
        if len_b % 2 == 0:
            max_o += len_b // 2
        else:
            max_o += math.ceil(len_b / 2)
        
    # max_o == K
    # 偶数区間を'?'のまま
    # 奇数区間を'o.o'に変換

    if max_o == K:
        parts = re.findall(r'[o.]+|\?+', ''.join(S2))
        ANS = ''
        for part in parts:
            if part[0] != '?':
                ANS += part
            else:
                if len(part) % 2 == 0:
                    ANS += part
                else:
                    ANS += 'o.' * (len(part) // 2) + 'o'
        print(ANS)
        return

    # max_o > K
    if max_o > K:
        print(''.join(S2))
        return

    

    






if __name__ == "__main__":
    main()

# 全探索でTLE
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# mod = 10**9

# from collections import deque
# def main():
#     N, K = map(int, stdin.readline().split())
#     S = stdin.readline().rstrip()

#     S2 = [S[0]]
#     for idx, s in enumerate(S):
#         if idx == 0:
#             continue
#         if s == '?' and S[idx-1] == 'o':
#             S2.append('.')
#         elif s == '?' and idx+1 < N and S[idx+1] == 'o':
#             S2.append('.')
#         else:
#             S2.append(s)

#     count_q = 0
#     count_o = 0
#     for s in S2:
#         if s == '?':
#             count_q += 1
#         elif s == 'o':
#             count_o += 1
#         else:
#             continue
#     S2 = ''.join(S2)
#     ANS_SET = solve(0, S2, K, count_q, count_o)

#     ANS = ''
#     for idx in range(N):
#         s_idx = next(iter(ANS_SET))[idx]
#         for s in ANS_SET:
#             if s_idx != s[idx]:
#                 s_idx = '?'
#                 continue
#         ANS += s_idx

#     print(ANS)

    
# def solve(idx, S2, K, count_q, count_o):
#     if count_q == 0:
#         if count_o == K:
#             return {S2}
#         else:
#             return set()


#     if S2[idx] == '?':
#         o_flag = True # 'o'に変換できるか

#         if idx != 0 and S2[idx-1] == 'o':
#             o_flag = False
#         if idx != len(S2) - 1 and S2[idx+1] == 'o':
#             o_flag = False
#         if count_o == K:
#             o_flag = False
#         if o_flag:
#             S2_a = S2[:idx] + 'o' + S2[idx+1:]
#             S2_b = S2[:idx] + '.' + S2[idx+1:]
#             return solve(idx+1, S2_a, K, count_q-1, count_o+1) | solve(idx+1, S2_b, K, count_q-1, count_o)
#         else:
#             S2_b = S2[:idx] + '.' + S2[idx+1:]
#             return solve(idx+1, S2_b, K, count_q-1, count_o)
#     else:
#         return solve(idx+1, S2, K, count_q, count_o)

# if __name__ == "__main__":
#     main()


# WAになったNGパターン
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# mod = 10**9

# from collections import deque
# def main():
#     N, K = map(int, stdin.readline().split())
#     S = stdin.readline().rstrip()

#     S2 = [S[0]]
#     for idx, s in enumerate(S):
#         if idx == 0:
#             continue
#         if s == '?' and S[idx-1] == 'o':
#             S2.append('.')
#         elif s == '?' and idx+1 < N and S[idx+1] == 'o':
#             S2.append('.')
#         else:
#             S2.append(s)

#     count_q = 0
#     count_o = 0
#     for s in S2:
#         if s == '?':
#             count_q += 1
#         elif s == 'o':
#             count_o += 1
#         else:
#             continue
    
#     if count_q + count_o > K:
#         print(''.join(S2))
#     else:
#         for idx, s in enumerate(S2):
#             if s == '?':
#                 S2[idx] = 'o'
#             else:
#                 S2[idx] = s
#         print(''.join(S2))


# if __name__ == "__main__":
#     main()