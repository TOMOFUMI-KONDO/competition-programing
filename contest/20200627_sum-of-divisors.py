def main():
    n = int(input())

    sum = 0
    for j in range(n):
        j += 1
        k = n // j
        sum += (k * (1 + k) // 2) * j

    print(sum)


if __name__ == '__main__':
    main()
