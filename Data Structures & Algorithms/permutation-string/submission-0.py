class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        # Frequency arrays for all 26 lowercase English letters ('a' - 'z')
        s1Count, s2Count = [0] * 26, [0] * 26
        # Initialize character counts for s1 and the first window of s2 (size = len(s1))
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 # s[0] represents frequency of 'a'
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many character frequencies match exactly between s1 and the initial window
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # Slide the fixed-size window across s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # --- Add incoming character on the right (r) ---
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
            # Incrementing brought the count to the exact target
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                # Incrementing exceeded the target count, breaking a previous match
                matches -= 1

        # --- Remove outgoing character on the left (l) ---
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                # Decrementing reduced an excess count back to the exact target
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                # Decrementing dropped below the target count, breaking a previous match
                matches -= 1
            
            l += 1

        # Check the match status for the very last window position
        return matches == 26
        