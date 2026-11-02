class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window_size = len(s1)
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        if len(s1) > len(s2):
            return False
        
        if s1_count == window_count:
            return True

        for r in range(len(s1), len(s2)):
            right_char = s2[r]
            window_count[right_char] += 1
            left_char = s2[r-len(s1)]
            window_count[left_char] -= 1

            if s1_count == window_count:
                return True

        return False
