import math
 
a, b, x = map(int, input().split())
 
cond = a*a*b
si = 0
if x == cond/2:
  print(45)
  exit(0)
elif x < cond/2:
  y = (2*x)/(a*b)
  si = math.atan(b/y)
elif x > cond/2:
  y = 2*b - (2*x)/(a**2)
  si = math.atan(y/a)
  
ans = math.degrees(si)
print(ans)