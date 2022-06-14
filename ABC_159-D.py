from collections import Counter
 
N = int(input())
A = list(map(int, input().split()))
 
XX = Counter(A)
#print(XX, cond)
cond = XX.keys()
 
 
count = 0
for j in cond:
  count += XX[j]*(XX[j]-1)//2
 
ans = 0
for g in A:
  ans = count - (XX[g] - 1)
  print(ans)