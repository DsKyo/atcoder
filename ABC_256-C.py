h1, h2, h3, w1, w2, w3 = map(int, input().split())
 
h_sum = h1 + h2 + h3
w_sum = w1 + w2 + w3
 
if h_sum != w_sum:
  print(0)
  exit(0)
  
cond = [[0]*3 for _ in range(3)]
count = 0
for i in range(1, h1-1):
  for j in range(1, h1-i):
    cond[0][0] = i
    cond[0][1] = j
    cond[0][2] = h1 - i - j
    for k in range(1, h2-1):
      for h in range(1, h2-k):
        cond[1][0] = k
        cond[1][1] = h
        cond[1][2] = h2 - k - h
        for g in range(1, h3-1):
            for f in range(1, h3-g):
              cond[2][0] = g
              cond[2][1] = f
              cond[2][2] = h3 - g - f
              if i + k + g == w1 and j + h + f == w2 and cond[0][2] + cond[1][2] + cond[2][2] == w3:
                count += 1
          
print(count) 