x = input()

from decimal import Decimal, getcontext

# Decimalの精度を設定
getcontext().prec = 50
x = Decimal(x)

print(int(x))

