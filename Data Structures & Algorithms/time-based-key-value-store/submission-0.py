from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            mid_val, mid_time = values[mid]

            if mid_time <= timestamp:
                res = mid_val
                l = mid + 1
            else:
                r = mid - 1
        return res
