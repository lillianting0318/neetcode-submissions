class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        for num, freq in count.most_common(k):
            res.append(num)

        return res