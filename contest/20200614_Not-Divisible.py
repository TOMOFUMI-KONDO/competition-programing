def main():
    _ = int(input())
    A = list(map(int, input().split()))

    A.sort()
    a_max = A[-1]
    dp = [0] * (a_max + 1)

    for a in A:
        if dp[a] != 0:
            dp[a] = 2
            continue

        i = a
        while i < a_max + 1:
            dp[i] += 1
            i += a

    r = 0
    for a in A:
        if dp[a] == 1:
            r += 1

    print(r)


if __name__ == '__main__':
    main()