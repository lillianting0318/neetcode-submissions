class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = max(count.values())

        max_count = sum (1 for freq in count.values() if freq == max_freq)

        res = (max_freq - 1) * (n + 1) + max_count

        return max(res, len(tasks))