from itertools import product


arr = [1, 2, 3]
# 全ての組み合わせを生成
combinations = list(product(arr, repeat=2))
print(combinations)  # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
