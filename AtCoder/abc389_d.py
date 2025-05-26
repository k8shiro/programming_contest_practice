from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

R = -1

def main():
    global R
    R = int(stdin.readline())

    kyokai_set = [(R, 0)]
    y = 0
    for x in range(R-1, -1, -1):
        for add_y in range(R):
            if check(x, y + add_y) == 'kyokai':
                kyokai_set.append((x, y + add_y))
                y += add_y
                break

    sum_90_degree = 0
    for x, y in kyokai_set[:-1]:
        sum_90_degree += y
    ans = sum_90_degree * 4 + 1
    # print(kyokai_set)
    print(ans)

    



    

# (0, 0)から半径Rの円に含まれるかを判定する
def check(x, y):
    global R
    xa = x + 0.5
    ya = y + 0.5
    xb = x + 0.5
    yb = y - 0.5
    xc = x - 0.5
    yc = y + 0.5
    xd = x - 0.5
    yd = y - 0.5
    a = (xa * xa + ya * ya) < (R * R)
    b = (xb * xb + yb * yb) < (R * R)
    c = (xc * xc + yc * yc) < (R * R)
    d = (xd * xd + yd * yd) < (R * R)
    x = int(a) + int(b) + int(c) + int(d)
    if x == 0:
        return 'soto'
    if x == 4:
        return 'naka'
    return 'kyokai'




if __name__ == "__main__":
    main()

# 全探索でTLE
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# in_circle = set()
# R = -1

# def main():
#     global R
#     R = int(stdin.readline())
#     search(0, 0)
#     print(len(in_circle))

# # (0, 0)から半径Rの円に含まれるかを判定する
# def check(x, y):
#     global in_circle
#     global R
#     if (x, y) in in_circle:
#         return True
#     xa = x + 0.5
#     ya = y + 0.5
#     xb = x + 0.5
#     yb = y - 0.5
#     xc = x - 0.5
#     yc = y + 0.5
#     xd = x - 0.5
#     yd = y - 0.5
#     a = (xa * xa + ya * ya) <= (R * R)
#     b = (xb * xb + yb * yb) <= (R * R)
#     c = (xc * xc + yc * yc) <= (R * R)
#     d = (xd * xd + yd * yd) <= (R * R)
#     if a and b and c and d:
#         in_circle.add((x, y))
#         return True
#     else:
#         return False

# # 右方向か上方向に探索する
# def search(x, y):
#     # 探索済みなら終了
#     if (x, y) in in_circle:
#         return

#     if check(x, y):
#         search(x + 1, y)
#         search(x, y + 1)
#         search(x - 1, y)
#         search(x, y - 1)
#     else:
#         return

# if __name__ == "__main__":
#     main()