def main():
    n, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sum_A = [0]
    sum_B = [0]

    for i in range(n):
        sum_A.append(sum_A[i] + A[i])

    for i in range(m):
        sum_B.append(sum_B[i] + B[i])

    r = 0
    j = m

    for i in range(n + 1):
        a = sum_A[i]
        if a > k:
            break

        while j > -1:
            if sum_B[j] > k - a:
                j -= 1
            else:
                r = max(r, i + j)
                break

    print(r)


if __name__ == '__main__':
    main()
