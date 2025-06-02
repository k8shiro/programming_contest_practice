print("行列")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    print(*row)

print("90度回転")
rotated = [list(reversed(col)) for col in zip(*matrix)]
for row in rotated:
    print(*row)