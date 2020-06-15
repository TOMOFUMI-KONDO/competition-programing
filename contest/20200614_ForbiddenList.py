import sys


def main():
    x, n = map(int, input().split())
    P = list(map(int, input().split()))

    if not (x in P):
        print(x)
        sys.exit()

    for i in range(101):
        x1 = max(0, x - (i + 1))
        x2 = min(101, x + (i + 1))

        if x1 == 0:
            print(0)
            sys.exit()
            
        if not (x1 in P):
            print(x1)
            sys.exit()

        if x2 == 101:
            print(101)
            sys.exit()
            
        if not (x2 in P):
            print(x2)
            sys.exit()


if __name__ == '__main__':
    main()
