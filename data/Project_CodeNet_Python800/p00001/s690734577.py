result = [0, 0, 0] 
for i in range(10):
 inp = int(raw_input())
 if result[2] >= inp:
  continue
 elif result[1] >= inp > result[2]:
  result[2] = inp
 elif result[0] >= inp > result[1]:
  result[2] = result[1]
  result[1] = inp
 else:
  result[2] = result[1]
  result[1] = result[0]
  result[0] = inp


for i in range(3):
 print result[i]