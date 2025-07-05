from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

from decimal import Decimal

# メモ化
from functools import lru_cache

# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18

# 10^9 + 7
MOD = 10**9 + 7


def main():
    L, R = map(int, stdin.readline().strip().split())

    # √R までの素数を列挙
    primes = sieve(int(R**0.5) + 1)
    set_primes = set(primes)


    L_R = [1] * (R - L + 1) 

    for num in range(L, R + 1):
        for p in set_primes:
            if num % p == 0:
                L_R[num - L] = 0
                break

    L_R[0] = 1
    for p in set_primes:
        num = p
        count = 1
        while num <= R:
            if num >= L:
                L_R[num - L] = 1
            num = num * p

    ans = sum(L_R)
    print(ans)
    # print(set_primes)
    # print(L_R)




    
        


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0と1は素数ではない

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    primes = [i for i, val in enumerate(is_prime) if val]
    return primes


if __name__ == "__main__":
    main()


# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# from decimal import Decimal

# # メモ化
# from functools import lru_cache

# # 探索失敗用にINT_MAXを定義
# INT_MAX = 10**18

# # 10^9 + 7
# MOD = 10**9 + 7


# def main():
#     L, R = map(int, stdin.readline().strip().split())
#     nums = list(range(1, L+1))
#     ANS = []
#     ANS.append(lcm_multiple(nums))
#     # print(ANS)

#     factors_set = set()
#     for x in range(L+1):
#         factors = prime_factorization(x)
#         for f in factors:
#             factors_set.add(f)

#     # print(factors_set)


#     for x in range(L+1, R+1):
#         ans = ANS[-1]
#         factors = prime_factorization(x)
#         for f in factors:
#             if f not in factors_set:
#                 factors_set.add(f)
#                 ans *= f[0]

#         ANS.append(ans)

#     print(len(set(ANS)))



# import math
# from functools import reduce

# def lcm_multiple(numbers):
#     return reduce(lambda x, y: math.lcm(x, y), numbers)

# from collections import defaultdict
# def prime_factorization(n):
#     factors = []
#     divisor = 2
#     while divisor * divisor <= n:
#         while n % divisor == 0:
#             factors.append(divisor)
#             n //= divisor
#         divisor += 1
#     if n > 1:
#         factors.append(n)
    
#     # インデックス付け
#     count = defaultdict(int)
#     result = []
#     for f in factors:
#         count[f] += 1
#         result.append((f, count[f]))
#     return result




# if __name__ == "__main__":
#     main()