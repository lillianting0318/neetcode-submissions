class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket n: freq
        # Bucket 1: 3
        # Bucket 2: 2
        # Bucket 3: 1
        # bucket = {1: 3, 2: 2, 3: 1}
        bucket = {}
        for n in nums:
            bucket[n] = 1 + bucket.get(n, 0)

        rank = []
        for n, freq in bucket.items():
            rank.append([freq, n])  

        rank.sort(reverse=True)    # sort ascending: rank = [[3, 1], [2, 2], [1, 3]]

        res = []
        for i in range(k):
            res.append(rank[i][1])

        return res
