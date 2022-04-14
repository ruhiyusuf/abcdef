def transpose(srcList, destList): 
  # convert variable length list to 2D list of same length
  m = max(map(lambda srcList: len(srcList), srcList))
  for i in range(0, len(srcList)):
    while len(srcList[i]) < m:
      srcList[i].append('')

  for i in range(0, len(srcList[0])):
    row = []
    for item in srcList: 
      row.append(item[i])
    destList.append(row)
    
  return destList

x = [['a','d','g'],['b','e', 'z'],['c','f', 'y', 'x', 'z']]
y = []
transpose(x, y)
print(x)
print(y)

for row in y: 
  print("{: >20} {: >20} {: >20}".format(*row))