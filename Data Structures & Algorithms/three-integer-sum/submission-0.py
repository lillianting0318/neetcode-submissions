class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # if the first number is greater than 0, then it will not be equal to 0 with the rest numbers
            if nums[i] > 0:
                break
            # remove duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # two sum
            l, r = i + 1, n - 1
            while l < r:    # l and r cannot be equal
                threeSum = nums[l] + nums[r] + nums[i]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # if found a solution, r and l pointer should shift inner because if shift one of them will make the sum greater or smaller than 0
                    r -= 1
                    l += 1
                    # prevent from duplicate like [-2, 0, 0, 2, 2]
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res

                    

