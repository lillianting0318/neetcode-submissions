class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_count = Counter(t)
        required = len(t_count) # required char
        l, r = 0, 0
        formed = 0  # window char
        window_count = {}

        res = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # update minimum
            while l <= r and formed == required:
                character = s[l]
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)

                window_count[character] -= 1
                if character in t_count and window_count[character] < t_count[character]:
                    formed -= 1
                l += 1
            r += 1

        if res[0] == float("inf"):
            return ""
        else:
            return s[res[1]:res[2]+1]




