import collections


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    q = int(input())

    CNT = [0] * (10 ** 5)

    C = collections.Counter(A)
    for k, v in C.items():
        CNT[k - 1] = v

    s = 0
    for i in range(10 ** 5):
        s += (i + 1) * CNT[i]

    # S = []
    for i in range(q):
        b, c = map(int, input().split())
        value = CNT[b - 1]
        CNT[b - 1] = 0
        CNT[c - 1] += value

        s = s - b * value + c * value
        print(s)


if __name__ == '__main__':
    main()
