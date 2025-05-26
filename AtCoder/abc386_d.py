from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    N, M = map(int, stdin.readline().split())

    XYC = []
    for _ in range(M):
        X, Y, C = map(str, stdin.readline().split())
        X = int(X)
        Y = int(Y)
        XYC.append((X, Y, C))
    
    # XYCをソート
    # Xの降順で、同じXの場合はCが'B'の場合が先に来るように
    XYC.sort(key=lambda x: (x[0], x[2] == 'B'), reverse=True)
    # print(XYC)

    black_y = 0
    for x, y, c in XYC:
        if c == 'B':
            black_y = max(black_y, y)
        else:  # c == 'W'
            if y <= black_y:
                print("No")
                return
    print("Yes")



if __name__ == "__main__":
    main()

# WAのパターン
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)


# # 探索失敗用にINT_MAXを定義
# INT_MAX = 10**18


# def main():
#     N, M = map(int, stdin.readline().split())

#     XYC = []
#     for _ in range(M):
#         X, Y, C = map(str, stdin.readline().split())
#         X = int(X)
#         Y = int(Y)
#         XYC.append((X, Y, C))
    
#     # XYCをXの昇順にソート
#     # Xが同じ場合はCが'W'が先に来るように
#     XYC.sort(key=lambda x: (x[0], x[2] == 'B'), reverse=False)

#     # X, Cが同じ入力を持つ場合は、Yの値を比較して
#     # 'W'のYが最小になるようにする
#     # 'B'のYは最大になるようにする
#     _XYC = []
#     for x, y, c in XYC:
#         # _XYCが空の場合は追加
#         if not _XYC:
#             _XYC.append((x, y, c))
#             continue
#         # 最後の要素と比較
#         last_x, last_y, last_c = _XYC[-1]
#         if last_x == x and last_c == c:
#             # 同じX, Cの場合はYを比較
#             if c == 'W':
#                 # 'W'のYが最小になるように
#                 if y < last_y:
#                     _XYC[-1] = (x, y, c)
#             else:
#                 # 'B'のYが最大になるように
#                 if y > last_y:
#                     _XYC[-1] = (x, y, c)
#         else:
#             # 異なるX, Cの場合は追加
#             _XYC.append((x, y, c))

#     XYC = _XYC

#     black_y = N
#     for x, y, c in XYC:
#         if c == 'W':
#             new_black_y = y - 1
#             if new_black_y <= black_y:
#                 black_y = new_black_y
#             else:
#                 print("No")
#                 return
#         else:  # c == 'B'
#             if y > black_y:
#                 print("No")
#                 return
#     print("Yes")



# if __name__ == "__main__":
#     main()