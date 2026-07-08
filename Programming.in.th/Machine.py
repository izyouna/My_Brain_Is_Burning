import heapq
import sys
input = sys.stdin.readline

n = int(input())
ans = []

for i in range(n):
  arr = input().split()
  if arr[0] == 'P':
    value = int(arr[1])
    heapq.heappush(ans, -value) 
  else:
    print(-heapq.heappop(ans) if ans else -1)