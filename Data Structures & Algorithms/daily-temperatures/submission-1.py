class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for curr_i, curr_t in enumerate(temperatures):
            while stack and curr_t > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                res[prev_i] = curr_i - prev_i

            stack.append((curr_t, curr_i))

        return res