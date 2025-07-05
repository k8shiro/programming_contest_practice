 

def main():
    L, R = map(int, input().split())
    size = R - L  # L+1 から R までなので R-L 個
    vis = [0] * size  # 処理済みフラグ（L+1+i の i 番目）

    ans = 1  # y==1 だった数のカウント（1個確実にある前提）
    for p in prime_enumerate(int(math.sqrt(R)) + 1):
        # x: L+1 以上で最小の p の倍数
        start = ((L // p) + 1) * p
        for x in range(start, R + 1, p):
            idx = x - (L + 1)
            if idx < 0 or idx >= size:
                continue
            if vis[idx]:
                continue
            vis[idx] = 1
            y = x
            while y % p == 0:
                y //= p
            if y == 1:
                ans += 1

    # vis[i] == 0 → どの素数でも割られていない → y==iが素数 or 素数の1つ
    for v in vis:
        if v == 0:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
