import numpy as np
from itertools import product
 
N, M, X = map(int, input().split())
      
books = []
C = []
Al = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  books.append(tmp)
  C.append(tmp[0])
  Al.append(tmp[1:])
  
 
ans = 10**8
for bits in product([0, 1], repeat=N):
  count = [0]*M
  price = 0
  for i in range(N):
    if bits[i]:
      count = np.add(count, Al[i])
      price = price + C[i]
  if min(count) >= X:
    ans = min(ans, price)
    
if ans == 10**8:
  print(-1)
else:
  print(ans)