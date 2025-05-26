from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    S = str(stdin.readline().strip())

    count = 0
    change_count = 0
    for s in S[::-1]:
        s = (int(s) - change_count) % 10
        count += s + 1
        change_count += s

    print(count)



if __name__ == "__main__":
    main()

# TLEのパターン
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)


# # 探索失敗用にINT_MAXを定義
# INT_MAX = 10**18

# # 変換表（str -> str）
# # x == 1の時
# # CONVERT_TABLE = str.maketrans({
# #     '0': '9',
# #     '1': '0',
# #     '2': '1',
# #     '3': '2',
# #     '4': '3',
# #     '5': '4',
# #     '6': '5',
# #     '7': '6',
# #     '8': '7',
# #     '9': '8'
# # })
# def create_convert_table(x):
#     tmp = {
#         '0': str((0 - x) % 10),
#         '1': str((1 - x) % 10),
#         '2': str((2 - x) % 10),
#         '3': str((3 - x) % 10),
#         '4': str((4 - x) % 10),
#         '5': str((5 - x) % 10),
#         '6': str((6 - x) % 10),
#         '7': str((7 - x) % 10),
#         '8': str((8 - x) % 10),
#         '9': str((9 - x) % 10)
#     }

#     convert_table = str.maketrans(tmp)
#     return convert_table

# CONVERT_TABLE = [create_convert_table(i) for i in range(10)]
# #print(CONVERT_TABLE)




# def main():
#     S = str(stdin.readline().strip())

#     count = 0
#     while True:
#         if S == "0":
#             count += 1
#             break
        
#         if S[-1]  != "0":
#             s = int(S[-1])
#             # SをボタンBを押す前に戻す
#             S = S.translate(CONVERT_TABLE[s])
#             count += s
#         else:
#             # SをボタンAを押す前に戻す
#             S = S[:-1]
#             count += 1
#     print(count)

# if __name__ == "__main__":
#     main()