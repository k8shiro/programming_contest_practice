"""
区間篩＋素因数順番付きの実装
指定区間の素因数分解
"""

import math

def segmented_factor_ordered(L, R):
    limit = int(math.isqrt(R)) + 1

    # エラトステネスで √R 以下の素数を列挙
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    size = R - L
    numbers = [L + 1 + i for i in range(size)]  # 対象整数列
    factors = [[] for _ in range(size)]         # 素因数のリスト（重複あり）

    for p in primes:
        # 最初の p の倍数 >= L+1 を求める
        start = max(p * p, ((L + 1 + p - 1) // p) * p)
        for j in range(start, R + 1, p):
            idx = j - (L + 1)
            while numbers[idx] % p == 0:
                factors[idx].append(p)
                numbers[idx] //= p

    for i in range(size):
        if numbers[i] > 1:
            factors[i].append(numbers[i])  # 残った素数も追加

    # 出現順に変換（例：2,2,3 -> [(2,1),(2,2),(3,1)])
    result = []
    for i in range(size):
        count = {}
        ordered = []
        for p in factors[i]:
            count[p] = count.get(p, 0) + 1
            ordered.append((p, count[p]))
        result.append((L + 1 + i, ordered))

    return result




res = segmented_sieve_prime_factors_with_order(10, 20)
for n, facs in res:
    print(f"{n} -> {facs}")
