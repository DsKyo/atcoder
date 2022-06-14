N, K = map(int, input().split())
P = list(map(int, input().split()))
 
cond = 0
for i in range(K):
  cond += (P[i]+1)/2
  
ans = cond
for i in range(K, N):
  cond = cond + (P[i]+1)/2 - (P[i-K]+1)/2
  ans = max(ans, cond)         
           
print(ans)