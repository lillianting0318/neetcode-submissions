class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n
        
        pref[0] = suff[n - 1] = 1
        
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
        for i in range(1, n):
            suff[n - 1 - i] = suff[n - i] * nums[n - i]
        for i in range(n):
            res[i] = pref[i] * suff[i]
            
        return res