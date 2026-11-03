class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # store indices of elements in decreasing order

        for r in range(len(nums)):
            # q not empty and list tail less than current nums[r] => pop it
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if q[0] < r - k + 1:
                q.popleft()
            
            if r >= k - 1:
                res.append(nums[q[0]])

        return res