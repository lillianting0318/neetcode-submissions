class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prev_temp, prev_i = stack.pop()
                res[prev_i] = i - prev_i

            stack.append((t, i))
            
        return res