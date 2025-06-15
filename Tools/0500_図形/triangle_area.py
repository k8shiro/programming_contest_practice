"""
三角形の面積を計算する関数
三角形の頂点座標を引数として受け取り、面積を返す。
"""

def triangle_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

# 使用例
A = (0, 0)
B = (4, 0)
C = (0, 3)

area = triangle_area(A, B, C)
print(f"三角形の面積: {area}")

A = (0, 0)
B = (-4, 0)
C = (0, -3)

area = triangle_area(A, B, C)
print(f"三角形の面積: {area}")
