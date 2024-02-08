n = int(input())

a_list = []

max_1 = -1
max_2 = -2
for _ in range(n):
    a = int(input())
    a_list.append(a)

    if a > max_1:
        max_2 = max_1
        max_1 = a
    elif a > max_2:
        max_2 = a

for a in a_list:
    if a == max_1:
        print(max_2)
    else:
        print(max_1)

