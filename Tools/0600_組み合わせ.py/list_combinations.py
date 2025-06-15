"""
リストから3点の組み合わせを列挙する
"""
from itertools import combinations

points = [(0, 0), (1, 0), (0, 1), (2, 2)]

# 3点の組み合わせを列挙
triplets = list(combinations(points, 3))

for triplet in triplets:
    print(triplet)
