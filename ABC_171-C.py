N = int(input())
 
a = [chr(ord("a")+i) for i in range(26)]
ans = ''
while N > 0:
  N = N-1
  m = N%26
  ans = a[m] + ans
  N = N//26
 
print(ans)