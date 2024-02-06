from decimal import Decimal, getcontext

# Decimalの精度を設定
getcontext().prec = 50



from sys import stdin
a, b = map(str, stdin.readline().split())
a = Decimal(a)
b = Decimal(b)

print(int(a*b))

