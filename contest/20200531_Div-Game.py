import sys
import copy
import collections

# 素因数分解の結果をlistで返す
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    n = int(input())
    n_prime = prime_factorize(n)
    unique_n_prime = []
    unique_n_prime = [x for x in n_prime if x not in unique_n_prime and not unique_n_prime.append(x)]

    ans = 0
    ans += len(unique_n_prime)

    unique_c = collections.Counter(unique_n_prime)

    c = collections.Counter(n_prime)
    c = c - unique_c
    t = 1
    while len(c) > 0:
        for _ in range(t):
            c = c - unique_c
        ans += len(c)
        c = c - unique_c
        t += 1

    print(ans)



if __name__ == '__main__':
    main()