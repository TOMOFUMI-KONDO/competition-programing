# bubble sort
A = list(input().split())
len_A = len(A)  
B = list(A)
C = list(A)

for i in range(len_A): 
  for j in reversed(range(i+1, len_A)):
    if B[j] < B[j-1]:
      tmp = B[j]
      B[j] = B[j-1]
      B[j-1] = tmp


# select sort
for i in range(len_A):
  min = i
  for j in range(i, len_A):
    if C[j] < C[min]:
      min = j
  
  if min != i:
    tmp = C[min]
    C[min] = C[i]
    C[i] = tmp

# insertin sort
def insertionSort(A, n, g, cnt):
  for i in range(g,n):
    v = A[i]
    j = i - g
    
    while j >= 0 and A[j] > v:
      A[j+g] = A[j]
      j = j - g   
      cnt += 1

    A[j+g] = v

  return [A, cnt]

# shell sort
def shellSort(A, n):
  cnt = 0

  G = [1]
  i = 1
  while G[0] + 3 ** i < n:
    G.insert(0, G[0] + 3 ** i)
    i += 1

  m = len(G)

  for i in range(m):
    A, cnt = insertionSort(A, n, G[i], cnt)

  return [m, G, A, cnt]
