side = 3
arrMatrix = [[i+1+side*j for i in range(side)] for j in range(side)]

for i in range(side):
  print(*arrMatrix[i])

