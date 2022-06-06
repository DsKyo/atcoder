N, K = map(int, input().split())
 
A = list(map(int, input().split()))
 
#最終-1列まで判定
cond = []
for i in range(K):
  cond.append(sorted(A[i::K]))
 
for j in range(N//K):
  for h in range(K-1):   
    if cond[h][j] > cond[h+1][j]:
      print('No')
      exit(0)
      
#最終列のみ判定      
lr = N - (N//K*K)
cond_l = []
for u in range(lr):
  cond_l.append(cond[u][-1])
 
for t, r in enumerate(cond_l):
  if t == 0:
    tmp = r
  else:
    if tmp > r:
      print('No')
      exit(0)
    else:
      tmp = r
 
print('Yes')