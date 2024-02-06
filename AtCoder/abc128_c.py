from sys import stdin
n, m = map(int, stdin.readline().split())

switches = []
for i in range(m):
    ks = map(int, stdin.readline().split())
    ks = list(ks)
    switches.append(ks[1:])

p = map(int, stdin.readline().split())
p = list(p)



bit = 0
ans = 0
while bit < (1 << n):
    #print("bit", bit, bin(bit))
    
    all_onoff = True
    for i in range(m):
        p_i = p[i]
        switches_i = switches[i]

        onoff = 0
        for switch in switches_i:
            #print("switch", switch, bin(1 << (switch - 1)))
            if bit & (1 << (switch - 1)):
                onoff += 1

        #print("onoff", bin(bit), switches_i, onoff)
        if onoff % 2 != p_i:
            all_onoff = False
            break

    if all_onoff:
        ans += 1

    bit += 1
print(ans)




