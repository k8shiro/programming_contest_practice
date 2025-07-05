def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0と1は素数ではない

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    primes = [i for i, val in enumerate(is_prime) if val]
    return primes


print(sieve(30))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]