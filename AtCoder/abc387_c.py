from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


def main():
    L, R = map(int, stdin.readline().split())

    ANS = count_snake(R) - count_snake(L - 1)
    print(ANS)

# num以下のヘビ数を数える
def count_snake(N):
    digits = list(map(int, str(N)))
    n = len(digits)

    from functools import lru_cache

    @lru_cache(None)
    def dfs(pos, tight, head, has_head, max_other):
        if pos == n:
            # 条件: head > max_other
            return int(has_head and head > max_other)

        res = 0
        limit = digits[pos] if tight else 9

        for d in range(0, limit + 1):
            next_tight = tight and (d == limit)
            if not has_head and d == 0:
                # まだ先頭に到達してない (スキップ可能)
                res += dfs(pos + 1, next_tight, head, False, max_other)
            elif not has_head:
                # 最初の非ゼロ桁 = head 候補
                res += dfs(pos + 1, next_tight, d, True, -1)
            else:
                # それ以降の桁（headは確定済）
                res += dfs(pos + 1, next_tight, head, True, max(max_other, d))

        return res

    return dfs(0, True, -1, False, -1)









if __name__ == "__main__":
    main()


# たぶんTLE
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)


# def main():
#     L, R = map(int, stdin.readline().split())

#     # Rの桁数を取得
#     R_digit = len(str(R))
#     ANS = 0

#     from collections import deque
#     for check_digit in range(2, R_digit + 1):
#         snake = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
#         while snake:
#             # 先頭の数字を取り出す
#             num = snake.popleft()
#             num_digit = len(str(num))

#             # 取り出した数字の桁数がcheck_digitと一致する場合
#             if num_digit == check_digit:
#                 # numがL以上R以下の場合
#                 if L <= num <= R:
#                     ANS += 1
#                 continue
#             else:
#                 head = int(str(num)[0])
#                 for i in range(head):
#                     snake.append(num * 10 + i)
#     print(ANS)

# if __name__ == "__main__":
#     main()