from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
ANS = set()

def search(idx=0, A_SUM=[]):
    if idx == N:
        xor = A_SUM[0]
        for idx in range(len(A_SUM)):
            if idx == 0:
                continue
            xor ^= A_SUM[idx]
        ANS.add(xor)
        return

    xor = set()
    # for i in range(len(A_SUM)):
    #     _A_SUM = A_SUM[:]
    #     _A_SUM[i] += A[idx]
    #     xor |= search(idx + 1, _A_SUM)
    # _A_SUM = A_SUM[:]
    # _A_SUM.append(A[idx])
    # xor |= search(idx + 1, _A_SUM)
    for i in range(len(A_SUM)):
        A_SUM[i] += A[idx]
        search(idx + 1, A_SUM)
        A_SUM[i] -= A[idx] # 状態を戻す（バックトラック）
    A_SUM.append(A[idx])
    search(idx + 1, A_SUM)
    A_SUM.pop() # 状態を戻す（バックトラック）


search(0, [])
print(len(ANS))




# あってるがTLE
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# def main():
#     N = int(stdin.readline())
#     A = list(map(int, stdin.readline().split()))

#     def search(idx=0, A_SUM=[]):
#         if idx == N:
#             xor = A_SUM[0]
#             for idx in range(len(A_SUM)):
#                 if idx == 0:
#                     continue
#                 xor ^= A_SUM[idx]
#             return {xor}

#         xor = set()
#         # for i in range(len(A_SUM)):
#         #     _A_SUM = A_SUM[:]
#         #     _A_SUM[i] += A[idx]
#         #     xor |= search(idx + 1, _A_SUM)
#         # _A_SUM = A_SUM[:]
#         # _A_SUM.append(A[idx])
#         # xor |= search(idx + 1, _A_SUM)
#         for i in range(len(A_SUM)):
#             A_SUM[i] += A[idx]
#             xor |= search(idx + 1, A_SUM)
#             A_SUM[i] -= A[idx] # 状態を戻す（バックトラック）
#         A_SUM.append(A[idx])
#         xor |= search(idx + 1, A_SUM)
#         A_SUM.pop() # 状態を戻す（バックトラック）
#         return xor


#     xor = search(0, [])
#     print(len(xor))



# if __name__ == "__main__":
#     main()


# TLE 組み合わせ列挙後計算
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# import copy
# def main():
#     N = int(stdin.readline())
#     A = list(map(int, stdin.readline().split()))

#     A_GROUP = [
#         [[A[0]]]
#     ]
#     for idx in range(1, N):
#         # 次に追加する要素
#         a = A[idx]
#         NEXT_A_GROUP = []
#         for group in A_GROUP:
#             for i in range(len(group)):
#                 new_group = copy.deepcopy(group)
#                 new_group[i].append(A[idx])
#                 NEXT_A_GROUP.append(new_group)
#             new_group = copy.copy(group)
#             new_group.append([A[idx]])
#             NEXT_A_GROUP.append(new_group)
        
#         A_GROUP = NEXT_A_GROUP    
#         #print(A_GROUP)

#     xor = set()
#     for group in A_GROUP:
 
#         xor_ = sum(group[0])
#         for idx in range(len(group)):
#             if idx == 0:
#                 continue
#             xor_ ^= sum(group[idx])
#         xor.add(xor_)
#     print(len(xor))
        



# if __name__ == "__main__":
#     main()


# TLEの場合
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# import copy

# def main():
#     N = int(stdin.readline())
#     A = list(map(int, stdin.readline().split()))

#     # Aを1グループからNグループに分ける
#     xor = set()
#     for GROUP_NUM in range(N):
#         xor |= search(0, A, GROUP_NUM+1, [[] for _ in range(GROUP_NUM + 1)])
#     print(len(xor))



# def search(idx, A, GROUP_NUM, GROUP_LIST):
#     if idx == len(A):
#         # 空のグループのチェック
#         for g in GROUP_LIST:
#             if len(g) == 0:
#                 return set()
            
#         xor = sum(GROUP_LIST[0])
#         for idx in range(len(GROUP_LIST)):
#             if idx == 0:
#                 continue
#             xor ^= sum(GROUP_LIST[idx])
#         return {xor}
            

#     xor = set()
#     for g_n in range(GROUP_NUM):
#         GROUP_LIST[g_n].append(A[idx])
#         xor = xor | search(idx + 1, A, GROUP_NUM, GROUP_LIST)
#         GROUP_LIST[g_n].pop()  # 状態を戻す（バックトラック）
#     return xor


# if __name__ == "__main__":
#     main()