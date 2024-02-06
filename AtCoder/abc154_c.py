n = input()

from sys import stdin
a = map(int, stdin.readline().split())

list_a = list(a)
set_a = set(list_a)

if len(list_a) == len(set_a):
    print("YES")
else:
    print("NO")