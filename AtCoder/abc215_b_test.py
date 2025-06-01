# logとると失敗するので実際どこで失敗しているか見つける

from decimal import Decimal, getcontext
def solve_a(N):
    # getcontext().prec = 2000   # 精度を設定 1000では成功しない
    N = Decimal(N)
    log2n = N.log10() / Decimal(2).log10()
    ans = int(log2n)

    return ans, log2n

def solve_b(N):
    k = N.bit_length() - 1
    return k

def main():
    for n in range(1, 1000000000000000000):
        ans_a, log2n = solve_a(n)
        ans_b = solve_b(n)
        if ans_a != ans_b:
            print(f"log2n={log2n}, N={n}, ans_a={ans_a}, ans_b={ans_b}")
            break

if __name__ == "__main__":
    main()