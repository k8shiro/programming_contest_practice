n = int(input())

ans = set()

for _ in range(n):
    a = input()
    if a in ans:
        ans.remove(a)
    else:
        ans.add(a)

print(len(ans))