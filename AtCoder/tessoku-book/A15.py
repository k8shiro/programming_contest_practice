from sys import stdin

def main():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))

    A_SET = set(A)
    A_SORT = sorted(A_SET)
    A_DICT = {}
    for i, a in enumerate(A_SORT):
        A_DICT[a] = i + 1
    
    B = []
    for a in A:
        B.append(A_DICT[a])
    print(" ".join(map(str, B)))






if __name__ == "__main__":
    main()