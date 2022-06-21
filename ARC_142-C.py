N, K = map(int, input().split())
K_l = str(K)[-1]
 
if N < K or K_l == '0':
  print(0)
  exit(0)
  
cond = set()
rev = int(str(K)[::-1])
 
if K <= rev:
  while N >= K:
    cond.add(K)
    K = K*10
  
  while N >= rev:
    cond.add(rev)
    rev = rev*10
  
print(len(cond))