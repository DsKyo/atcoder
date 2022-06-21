N = int(input())
 
lists = [[0]*N for _ in range(N)]
num = 1
for i in range(N):
  for j in range(N):
    lists[i][j] = num
    num += 1
 
 
for i in range(1, N-1):
  for j in range(1, N, 2):
    tmp = lists[i][j-1]
    lists[i][j-1] = lists[i][j]
    lists[i][j] = tmp
    
for i in lists:
  print(*i)