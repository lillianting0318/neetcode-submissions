class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # dict (hash map)
        for num in nums:
            # count.get(num, 0): If num in dict, get the current count, if not, default 0
            count[num] = 1 + count.get(num, 0)  # count the frequency of every number
 
        # convert {num: cnt} to [cnt, num]
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        # put cnt at the first place so it can be stored by frequency
        arr.sort(reverse=True)

        # get the most kth frequent numbers
        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res