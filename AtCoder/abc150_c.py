n = int(input())
from sys import stdin

p = list(map(int, stdin.readline().split()))
q = list(map(int, stdin.readline().split()))

p = ''.join(map(str, p))
q = ''.join(map(str, q))

import itertools
a = None
b = None
cnt = 0
for jyunban in itertools.permutations(range(1, n+1), n):
    cnt += 1
    jyunban = ''.join(map(str, jyunban))
    if jyunban == p:
        a = cnt
    if jyunban == q:
        b = cnt

print(abs(a - b))