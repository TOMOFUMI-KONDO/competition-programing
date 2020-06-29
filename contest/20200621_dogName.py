import math


def main():
    alphabets = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z"]
    n = int(input())

    i = 1
    r = ''
    while True:
        r = alphabets[math.ceil((n % (26 ** i)) / (26 ** (i - 1))) - 1] + r
        if n - 26**i > 0:
            n -= 26**i
            i += 1
        else:
            break

    print(r)


if __name__ == '__main__':
    main()
