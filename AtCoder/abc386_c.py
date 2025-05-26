from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    K = int(stdin.readline().strip())
    S = str(stdin.readline().strip())
    T = str(stdin.readline().strip())

    if check(S, T):
        print("Yes")
    else:
        print("No")



def check(S, T):
    if len(S) != len(T):
        # 一旦Sのほうが長いようにする
        if len(S) < len(T):
            S, T = T, S
            
        # 差が1なら削除操作で一致させられる場合がある
        if len(S) - len(T) == 1:
            # Sのidx番目を削除してTと一致するか確認
            del_flag = False # 削除操作を行ったかどうか
            s_idx = 0
            t_idx = 0
            while s_idx < len(S) and t_idx < len(T):
                if S[s_idx] == T[t_idx]:
                    s_idx += 1
                    t_idx += 1
                else:
                    if del_flag:
                        # すでに削除操作を行った場合は一致しない
                        return False
                    else:
                        # 削除操作を行う
                        del_flag = True
                        s_idx += 1
            return True
        else:
            return False
    
    # SとTの長さが同じ場合
    # 違う個所を数える
    diff_count = 0
    for idx in range(len(S)):
        if S[idx] != T[idx]:
            diff_count += 1
    
    # 違う個所が1つ以下なら一致させられる
    if diff_count <= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    main()