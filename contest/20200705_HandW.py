def main():
  h, w, k = map(int, input().split())
  C = [list(input()) for _ in range(h)]

  result = 0
  for i in range(1 << h):
    for j in range(1 << w):
      cnt = 0
      for n in range(h):
        if i >> n & 1:
          continue

        for m in range(w):
          if j >> m & 1:
            continue

          if C[n][m] == '#':
            cnt += 1

      if cnt == k:
        result += 1

  print(result)


if __name__ == "__main__":
  main()
