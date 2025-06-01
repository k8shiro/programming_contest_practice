def main():
    for N in range(1, 1000000000000000000):

        import math
        log_2n_math = math.log2(N)
        log_2n_math = int(log_2n_math)  # 整数に変換
        # print(f'mathでのlog2(N) = {log_2n_math}')

        import decimal
        decimal.getcontext().prec = 100
        N_decimal = decimal.Decimal(N)
        log2n_decimal = N_decimal.log10() / decimal.Decimal(2).log10()
        log2n_decimal = int(log2n_decimal)
        # print(f'decimalでのlog2(N) = {log2n_decimal}')

        import numpy as np
        log2n_numpy = np.log2(N)
        log2n_numpy = int(log2n_numpy)
        # print(f'numpyでのlog2(N) = {log2n_numpy}')

        from mpmath import mp
        mp.dps = 100
        log2n_mpmath = mp.log(N, 2)
        log2n_mpmath = int(log2n_mpmath)
        # print(f'mpmathでのlog2(N) = {log2n_mpmath}')
        if log_2n_math == log2n_decimal == log2n_numpy == log2n_mpmath:
            continue
        else:
            print(f"Mismatch found for N={N}:")
            print(f"math.log2(N) = {log_2n_math}")
            print(f"decimal log2(N) = {log2n_decimal}")
            print(f"numpy log2(N) = {log2n_numpy}")
            print(f"mpmath log2(N) = {log2n_mpmath}")




if __name__ == "__main__":
    main()