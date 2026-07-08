num = int(input())
lst = []

for i in range(num):
  x = int(input())
  lst.append(x)

print(min(lst))
print(max(lst))