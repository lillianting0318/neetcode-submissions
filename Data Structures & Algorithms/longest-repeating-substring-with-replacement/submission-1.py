class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window_len - max_freq <= k
        count = {}     #hashmap
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            # count frequency of the char at right pointer 
            count[s[r]] = 1 + count.get(s[r], 0)
            # update maximum
            max_freq = max(max_freq, count[s[r]])
            
            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res