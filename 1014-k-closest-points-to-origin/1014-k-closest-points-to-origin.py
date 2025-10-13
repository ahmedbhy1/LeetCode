import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)
        for i in points:
            heapq.heappush(h,(i[0]**2 + i[1]**2,i))
        
        L = []
        for i in range(k):
            x = heapq.heappop(h)
            L.append(x[1])
        return L