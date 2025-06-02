from mpmath import mp
N = 64
mp.dps = 100
log2n_mpmath = mp.log(N, 2)
print(f'mpmathでのlog2(N) = {log2n_mpmath}')
