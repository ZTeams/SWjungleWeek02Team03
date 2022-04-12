import sys
import heapq

n = int(sys.stdin.readline())
max_h, min_h = [], []

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, (-num, num))
    else:
        heapq.heappush(min_h, (num, num))
    if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0][1] > min_h[0][1]:
        max_value = heapq.heappop(max_h)[1]
        min_value = heapq.heappop(min_h)[1]
        heapq.heappush(max_h, (-min_value, min_value))
        heapq.heappush(min_h, (max_value, max_value))
    print(max_h[0][1])
