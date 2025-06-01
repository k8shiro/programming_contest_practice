# 整数の 素因数分解
from sympy import factorint

n = 180
factors = factorint(n)
print(f"{n} の素因数分解: {factors}")


# 素数判定
from sympy import isprime

print(isprime(97))   # True
print(isprime(100))  # False


# 素数のリストを生成
from sympy import primerange, nextprime

print(list(primerange(10, 30)))  # 10〜30 の素数一覧
print(nextprime(100))           # 100より大きい最小の素数


# 最大公約数と最小公倍数
from sympy import gcd, lcm

print(gcd(18, 24))  # 6
print(lcm(18, 24))  # 72