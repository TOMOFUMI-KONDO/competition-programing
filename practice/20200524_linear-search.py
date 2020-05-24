import collections

def main():
  n = int(input())
  S = list(map(int, input().split()))
  q = int(input())
  T = list(map(int, input().split()))

  C = 0
  for t in T:
    if t in S:
      C += 1

  print(C)


if __name__ == '__main__':
  main()