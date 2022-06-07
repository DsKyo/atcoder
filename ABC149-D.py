N, K = map(int, input().split())
R, S, P = map(int, input().split())
 
T = input()
 
point = dict()
point['r'] = P
point['s'] = R
point['p'] = S
 
cond = []
for i in range(K):
  cond.append(T[i::K])
  
 
ans = 0
for i in range(K):
  count = 0
  for j in range(len(cond[i])):
    tmp_p = point[cond[i][j]]
    if j == 0:
      ans += tmp_p
    else:
      if cond[i][j] == cond[i][j-1]:
        count += 1
        ans += tmp_p
        if count%2 == 1:
          ans -= tmp_p
      else:
        count = 0
        ans += tmp_p
      
print(ans)