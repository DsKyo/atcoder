N = int(input())
S = input()
 
count_R = 0
set_R = set()
count_G = 0
set_G = set()
count_B = 0
set_B = set()
for a, i in enumerate(S):
  if i == 'R':
    count_R += 1
    set_R.add(a+1)
    
  if i == 'G':
    count_G += 1
    set_G.add(a+1)
 
  if i == 'B':
    count_B += 1
    set_B.add(a+1)
 
num = count_R*count_G*count_B
count = 0
for i in set_R:
  for j in set_G:
    if (i+j)/2 in set_B:
      count += 1
      
for i in set_G:
  for j in set_B:
    if (i+j)/2 in set_R:
      count += 1
      
for i in set_B:
  for j in set_R:
    if (i+j)/2 in set_G:
      count += 1
    
print(num - count)