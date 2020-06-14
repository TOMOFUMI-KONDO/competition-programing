import copy
import sys
import math

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * n

    for i in range(min(k, 41)):
        for j in range(n):
            l = max(0, j-A[j]) #座標iの電球が照らす範囲の左端
            r = min(n-1, j+A[j]) #座標iの電球が照らす範囲の右端
            B[l] += 1
            if (r+1 < n):
                B[r+1] -= 1 # 後ほど累積和にしたときに、照らす範囲の右端より外には影響が及ばないようにあらかじめ1引いておく

        for j in range(n-1):
            B[j+1] += B[j]

        A = copy.deepcopy(B)
        B = [0] * n

    print(*A)

if __name__ == '__main__':
    main()