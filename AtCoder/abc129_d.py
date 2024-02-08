# from sys import stdin

# def main():
#     h, w = list(map(int, stdin.readline().split()))

#     s = []
#     for i in range(h):
#         _s = stdin.readline()[:-1]
#         s.append(_s)

#     s_l = [[0] * w for _ in range(h)]
#     for i in range(h):
#         for j in range(w):
#             if s[i][j] == '#':
#                 s_l[i][j] = 0
#             elif j == 0:
#                 s_l[i][j] = 1
#             else:
#                 s_l[i][j] = s_l[i][j-1] + 1
    
#     s_r = [[0] * w for _ in range(h)]
#     for i in range(h):
#         for j in range(w-1, -1, -1):
#             if s[i][j] == '#':
#                 s_r[i][j] = 0
#             elif j == w-1:
#                 s_r[i][j] = 1
#             else:
#                 s_r[i][j] = s_r[i][j+1] + 1

#     s_t = [[0] * w for _ in range(h)]
#     for i in range(h):
#         for j in range(w):
#             if s[i][j] == '#':
#                 s_t[i][j] = 0
#             elif i == 0:
#                 s_t[i][j] = 1
#             else:
#                 s_t[i][j] = s_t[i-1][j] + 1

#     s_u = [[0] * w for _ in range(h)]
#     for i in range(h-1, -1, -1):
#         for j in range(w):
#             if s[i][j] == '#':
#                 s_u[i][j] = 0
#             elif i == h-1:
#                 s_u[i][j] = 1
#             else:
#                 s_u[i][j] = s_u[i+1][j] + 1

#     ans = 0
#     for i in range(h):
#         for j in range(w):
#             if s[i][j] == '#':
#                 continue
#             ans = max(ans, s_l[i][j]+s_r[i][j]+s_t[i][j]+s_u[i][j]-4+1)
#     print(ans)


# main()

from sys import stdin

def main():
    h, w = map(int, stdin.readline().split())

    s = [stdin.readline().strip() for _ in range(h)]

    s_l = [[0] * w for _ in range(h)]
    s_r = [[0] * w for _ in range(h)]
    s_t = [[0] * w for _ in range(h)]
    s_u = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s_l[i][j] = s_r[i][j] = s_t[i][j] = s_u[i][j] = 0
            else:
                s_l[i][j] = s_l[i][j-1] + 1 if j > 0 else 1
                s_t[i][j] = s_t[i-1][j] + 1 if i > 0 else 1

    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if s[i][j] == '#':
                s_r[i][j] = s_u[i][j] = 0
            else:
                s_r[i][j] = s_r[i][j+1] + 1 if j < w-1 else 1
                s_u[i][j] = s_u[i+1][j] + 1 if i < h-1 else 1

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            ans = max(ans, s_l[i][j]+s_r[i][j]+s_t[i][j]+s_u[i][j]-3)
    print(ans)


main()

