from decimal import Decimal, getcontext
# Decimalオブジェクトを使用するために精度を設定
getcontext().prec = 28

def calculate_distance(x1, y1, x2, y2):
    # 距離の計算 (ユークリッド距離)
    distance = ((x2 - x1)**2 + (y2 - y1)**2).sqrt()

    return distance




n = int(input())
from sys import stdin


xy = []
for _ in range(n):
    x, y = list(map(int, stdin.readline().split()))
    xy.append((x, y))


import itertools
cnt = 0
sum_d = 0
for jyunban in itertools.permutations(range(n), n):
    for i in range(n-1):
        x1, y1 = xy[jyunban[i]]
        x2, y2 = xy[jyunban[i+1]]
        sum_d += calculate_distance(Decimal(x1), Decimal(y1), Decimal(x2), Decimal(y2))
    cnt += 1

print(sum_d / cnt)