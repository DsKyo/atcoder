import math
 
N = int(input())
n = N
a = set()
while n % 2 == 0:
    a.add(2)
    n //= 2
f = 3
while f * f <= n:
    if n % f == 0:
        a.add(f)
        n //= f
    else:
        f += 2
if n != 1:
    a.add(n)
 
max_count = math.ceil(math.log(10**12, 2))
ans = 0
for i in a:
  for j in range(1, max_count):
    if N%(i**j) == 0:
      N = N//(i**j)
      ans += 1
      
print(ans)