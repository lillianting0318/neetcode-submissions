class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []   # stores (-distance_squared, [x, y])

        for x, y in points:
            dist_sq = x * x + y * y

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist_sq, [x, y]))
            else:
                if -dist_sq > max_heap[0][0]:
                    heapq.heappushpop(max_heap, (-dist_sq, [x, y]))
            
        return [pt for _, pt in max_heap]