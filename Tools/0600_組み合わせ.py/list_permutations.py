from itertools import permutations

lst = [1, 2, 3]

# 全ての順列を列挙
for p in permutations(lst):
    print(p)
