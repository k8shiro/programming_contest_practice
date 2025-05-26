from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    Q = int(stdin.readline())

    from collections import deque
    # 蛇格納用のdequeを作成
    dq = deque()
    # 全ての蛇の合計
    all_snake_sum = 0

    for _ in range(Q):
        query = list(map(int, stdin.readline().split()))
        if query[0] == 1:
            # 蛇を追加
            dq.append((query[1], all_snake_sum))
            all_snake_sum += query[1]
        elif query[0] == 2:
            # 先頭の蛇を抜く
            dq.popleft()
        else:
            left_snake = dq[0]
            right_snake = dq[query[1]-1]

            ans = right_snake[1] - left_snake[1]
            print(ans)
            









if __name__ == "__main__":
    main()