def main():
    N, D = map(int, input().split())
    walls = []
    
    for _ in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    
    # 壁を右端の位置でソート
    walls.sort(key=lambda x: x[1])
    
    punch_count = 0
    last_punch_end = -float('inf')
    
    for left, right in walls:
        if left > last_punch_end:
            punch_count += 1
            last_punch_end = right + D - 1
    
    print(punch_count)

if __name__ == "__main__":
    main()
