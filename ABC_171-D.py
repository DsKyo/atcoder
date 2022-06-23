from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

org = sum(A)
org_dict = dict(Counter(A))

for i in range(Q):
  b, c = map(int, input().split())
  if org_dict.get(b, 0) > 0:
    tmp = c-b
    count = org_dict[b]
    org += tmp*count
    org_dict[b] = 0
    if org_dict.get(c, 0) > 0:
      org_dict[c] += count
    else:
      org_dict[c] = count
  print(org)