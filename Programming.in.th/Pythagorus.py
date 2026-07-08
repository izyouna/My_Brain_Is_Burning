import math
x,y = map(float,input().split())
temp = x**2 + y**2
result = math.sqrt(temp)
print(f"{result:.6f}")