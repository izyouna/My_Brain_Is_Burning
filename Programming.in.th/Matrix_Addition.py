matrix1=[]
matrix2=[]
total=0
x,y= map(int,input().split())
for i in range(x):
  temp=list(map(int,input().split()))
  matrix1.append(temp)
for i in range(x):
  temp=list(map(float,input().split()))
  matrix2.append(temp)
for i in range(x):
  for j in range(y):
    total=matrix1[i][j]+matrix2[i][j]
    print(f"{total:g}",end=" ")
  print()