from sys import stdin
from collections import Counter
from fractions import Fraction


import sys
sys.setrecursionlimit(10**6)


from functools import lru_cache


INT_MAX = 10**18


MOD = 10**9 + 7


def main():

    T = int(stdin.readline().strip())

        
    testcases = []
    for _ in range(T):

        N = int(stdin.readline().strip())
        A = list(map(int, stdin.readline().strip().split()))
        testcases.append((N, A))


    for N, A in testcases:

        if N <= 2:
            print("Yes")
            continue

        A_counter = Counter(A)
        num_zeros = A_counter.get(0, 0)


        if num_zeros > 0:

            if len(A_counter) - 1 > 1:
                print("No")

            else:
                print("Yes")
            continue


        flag = False


        if len(A_counter) == 1:
            flag = True
        else:
            unique_A = sorted(list(A_counter.keys()))
            
            found_combination = False
            for i in range(len(unique_A)):
                for j in range(len(unique_A)):
                    if i == j:
                        continue
                    
                    a = unique_A[i]
                    b = unique_A[j]

                    r = Fraction(b, a)
                    
                    generated_seq = []
                    current_term = Fraction(a)
                    for _ in range(N):
                        if current_term.denominator != 1:
                            generated_seq = [] 
                            break
                        generated_seq.append(current_term.numerator)
                        current_term *= r

                    if Counter(generated_seq) == A_counter:
                        flag = True
                        found_combination = True
                        break
                if found_combination:
                    break
        
        if flag:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()