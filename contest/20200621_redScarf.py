def main():
    _ = int(input())
    A = list(map(int, input().split()))

    allXOR = 0
    for a in A:
        allXOR = allXOR ^ a  # 全てのスカーフの論理和

    R = []
    for a in A:
        R.append(a ^ allXOR)

    print(*R)


if __name__ == '__main__':
    main()
