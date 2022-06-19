N = int(input())
 
cond_L = []
cond_R = []
cond = []
for i in range(N):
  X = list(map(int, input().split()))
  cond.append(X)
cond.sort()
 
ans = []
ans.append(cond[0])
n = 0
for i in cond[1:]:
  if i[0] <= ans[n][1]:
    if ans[n][1] < i[1]:
      ans[n][1] = i[1]
  else:
    print(*ans[n])
    ans.append(i)
    n += 1
print(*ans[-1])