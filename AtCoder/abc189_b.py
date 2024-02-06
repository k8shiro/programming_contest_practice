from decimal import Decimal, getcontext

# Decimalの精度を設定
getcontext().prec = 50



from sys import stdin
n, x = map(int, stdin.readline().split())
x = Decimal(x)
alcoholic = Decimal(0)
for cnt in range(n):
    v, p = map(int, stdin.readline().split())
    alcoholic += Decimal(v) * Decimal(p) / Decimal(100)
    if alcoholic > x:
        print(cnt+1)
        exit()
print(-1) 