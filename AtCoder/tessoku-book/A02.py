from sys import stdin

def main():
    N, X = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))

    if X in A:
        print("Yes")
    else:
        print("No")

    return

if __name__ == "__main__":
    main()