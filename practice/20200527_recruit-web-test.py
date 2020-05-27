import sys


def main():
    n, m = map(int, input().split())
    floors = [list(input()) for _ in range(n)]

    now = [0,0]
    visit = [0 for _ in range(n*m)]
    visit_times = 0

    while True:
        i = now[0]
        j = now[1]

        if visit[i*m + j] == 1: # 同じところを訪れたら処理を終了
            break

        visit[i*m + j] = 1 # 訪れた場所を記録
        visit_times += 1

        direction = floors[i][j]
        if direction == 'N':
            i -= 1
        elif direction == 'S':
            i += 1
        elif direction == 'E':
            j += 1
        elif direction == 'W':
            j -= 1
        else:
            print('入力に誤りがあります。') #入力ルールに反していた場合、処理を終了
            sys.exit(1)

        if i < 0 or i > n-1 or j < 0 or j > m-1: # 壁にぶつかったら処理を終了
            break

        now = [i,j]

    print(visit_times)


if __name__ == '__main__':
    main()