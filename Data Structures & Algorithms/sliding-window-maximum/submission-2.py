class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # store indices of elements in decreasing order
        l = 0

        for r in range(len(nums)):
            # q not empty and list tail less than current nums[r] => pop it
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res