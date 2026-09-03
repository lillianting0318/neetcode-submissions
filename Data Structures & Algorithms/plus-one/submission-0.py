class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0   # one represents the 1 that needs to add

        while one:  # while one has not been added
            if i < len(digits):
                if digits[i] < 9:
                    digits[i] += 1
                    one = 0
                else:
                    digits[i] = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]