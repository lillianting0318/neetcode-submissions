class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        # Queue for remaining tasks
        q = deque()
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1   # pop the most frequent task in remaining tasks
                if cnt != 0:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time