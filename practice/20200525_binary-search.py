import sys

def main():
  n = int(sys.stdin.readline())
  S = list(map(int, sys.stdin.readline().split()))
  q = int(sys.stdin.readline())
  T = list(map(int, sys.stdin.readline().split()))

  C = 0
  
  for i in range(q):
    tmp = T[i]
    L = 0
    R = n - 1
    M = n // 2

    while M >= L:
      if tmp == S[M]:
        C += 1
        break
      elif tmp > S[M]:
        L = M + 1
      else:
        R = M - 1

      M = (R + L) // 2

  print(C)

if __name__ == '__main__':
  main()