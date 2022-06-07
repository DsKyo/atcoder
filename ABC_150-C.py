import itertools
 
N = int(input())
 
cond = [i for i in range(1, N+1)]
 
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
 
count = 0
P_count = 0
Q_count = 0
for per in itertools.permutations(cond, N):
  count += 1
  if per == P:
    P_count = count
  
  if per == Q:
    Q_count = count
    
ans = abs(P_count - Q_count)
print(ans)