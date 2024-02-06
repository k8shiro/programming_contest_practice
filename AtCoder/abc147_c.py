def check_bit(y, x):
    # yのxビット目が1か0かを判定する
    # xは0スタート
    bit_value = (y >> x) & 1
    return bit_value



n = int(input())

from sys import stdin

syogenn = [] # [(i, x, y)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, stdin.readline().split())
        syogenn.append((i+1, x, y))

max_value = 0
for bit in reversed(range(2 ** n)):
    #print("BIT", bin(bit))
    flag = True
    for i, x, y in syogenn:
        if check_bit(bit, i-1) == 0: # 不親切ならスキップ
            continue

        if y != check_bit(bit, x-1):
            flag = False
            break
    
    if flag:
        max_value = max(max_value, bin(bit).count("1"))
        

print(max_value)
            
