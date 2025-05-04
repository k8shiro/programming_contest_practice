from sys import stdin

def main():
    N, K = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))
    C = list(map(int, stdin.readline().split()))
    D = list(map(int, stdin.readline().split()))

    AB = set()
    for a in A:
        for b in B:
            AB.add(a + b)
    
    CD = set()
    for c in C:
        for d in D:
            CD.add(c + d)
    for ab in AB:
        if K - ab in CD:
            print("Yes")
            return
    print("No")




if __name__ == "__main__":
    main()