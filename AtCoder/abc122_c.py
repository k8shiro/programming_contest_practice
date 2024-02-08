from sys import stdin

n, q = list(map(int, stdin.readline().split()))
s = input()
l = []

# for i in range(q):
#     l, r = list(map(int, stdin.readline().split()))
#     print(s[l-1:r].count('AC'))

ac_count = [0] * n
for i in range(1, len(s)):
    if s[i-1] == 'A' and s[i] == 'C':
        ac_count[i] = ac_count[i-1] + 1
    else:
        ac_count[i] = ac_count[i-1]


for i in range(q):
    l, r = list(map(int, stdin.readline().split()))
    print(ac_count[r-1] - ac_count[l-1])

    

