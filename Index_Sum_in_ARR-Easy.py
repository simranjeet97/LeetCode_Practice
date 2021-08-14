sum = 24
res = []
s = set()
for i in range(n):
  temp = sum - arr[i]
  if (temp in s):
    res.append(arr[i])
    res.append(temp)
  s.add(arr[i])