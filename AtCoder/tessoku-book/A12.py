from sys import stdin

# 愚直にやってTLEのパターン
# def main():
#     N, K = map(int, stdin.readline().split())
#     A = list(map(int, stdin.readline().split()))

#     A = sorted(A)
#     TIMING = [0] * ((K+1) * A[0])
#     for a in A:
#         idx = 0
#         while True:
#             idx += a
#             if idx >= len(TIMING):
#                 break
#             TIMING[idx] += 1
    
#     SUM = 0
#     for idx in range(len(TIMING)):
#         SUM += TIMING[idx]
#         if SUM >= K:
#             print(idx)
#             return
            

# 少し改善もTLE
# def main():
#     N, K = map(int, stdin.readline().split())
#     A = list(map(int, stdin.readline().split()))

#     time_idx = 1
#     SUM = 0
#     while True:
#         for a in A:
#             if time_idx % a == 0:
#                 SUM += 1
#         if SUM >= K:
#             print(time_idx)
#             return
#         time_idx += 1

# 二分探索で求める
def main():
    N, K = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))

    A = sorted(A)
    TIME_R = K * A[0]
    TIME_L = 0
    
    while True:
        TIME_idx = (TIME_R + TIME_L) // 2
        SUM = 0
        for a in A:
            SUM += TIME_idx // a
        if SUM < K:
            TIME_L = TIME_idx + 1
        else:
            TIME_R = TIME_idx - 1
        
        if TIME_L > TIME_R:
            print(TIME_L)
            return

if __name__ == "__main__":
    main()