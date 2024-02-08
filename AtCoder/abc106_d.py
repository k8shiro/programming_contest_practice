
from sys import stdin
import numpy as np

# TLE
# def main():
#     n, m, q = map(int, stdin.readline().split())

#     lr = []
#     for i in range(m):
#         _l, _r = map(int, stdin.readline().split())
#         lr.append((_l, _r, i))

#     pq = []
#     p_set = set()
#     q_set = set()
#     for i in range(q):
#         _p, _q = map(int, stdin.readline().split())
#         pq.append([_p, _q])
#         p_set.add(_p)
#         q_set.add(_q)

#     lr_l = sorted(lr, key=lambda x: x[0])
#     idx = 0
#     city = 1
#     lr_l_dict = {}
#     while city <= n:
#         if city not in p_set:
#             city += 1
#             continue

#         if idx == m:
#             lr_l_dict[city] = set()
#             city += 1
#         elif lr_l[idx][0] >= city:
#             lr_l_dict[city] = set(lr_l[idx:])
#             city += 1
#         else:
#             idx += 1

#     #print(lr_l_dict)

#     lr_r = sorted(lr, key=lambda x: x[1])
#     lr_r.reverse()
#     idx = 0
#     city = n
#     lr_r_dict = {}
#     while city > 0:
#         if city not in q_set:
#             city -= 1
#             continue

#         if idx == m:
#             lr_r_dict[city] = set()
#             city -= 1
#         elif lr_r[idx][1] <= city:
#             lr_r_dict[city] = set(lr_r[idx:])
#             city -= 1
#         else:
#             idx += 1

#     #print(lr_r_dict)
#     for p, q in pq:
#         p_ans = lr_l_dict[p]
#         q_ans = lr_r_dict[q]
#         ans = len(p_ans & q_ans)
#         print(ans)


def main():
    n, m, q = map(int, stdin.readline().split())

    sorted_list = []
    for i in range(m):
        _l, _r = map(int, stdin.readline().split())
        sorted_list.append((_l, _r, -1))


    for i in range(q):
        _p, _q = map(int, stdin.readline().split())
        sorted_list.append((_p, _q, i+1))

    sorted_list.sort(key=lambda x: (x[1], x[2]))

    # print(sorted_list)

    count_list = [0] * (n+1)
    ans_list = []
    for l, r, order in sorted_list:
        if order != -1:
            ans = sum(count_list[l:r+1])
            ans_list.append((ans, order))
            
        else:
            count_list[l] += 1

    ans_list.sort(key=lambda x: x[1])
    for ans, _ in ans_list:
        print(ans)



main()