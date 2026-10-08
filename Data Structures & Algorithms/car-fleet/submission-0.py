class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds, then sort in descending order of position
        # We process cars from closest to farthest relative to the target
        pair = sorted(zip(position, speed), reverse=True)
        stack = []

        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            # If the current car (behind) arrives at or before the car ahead (stack[-2]),
            # it will catch up and merge into the same car fleet.
            # Pop the current car's time since it is constrained by the lead car's speed.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)