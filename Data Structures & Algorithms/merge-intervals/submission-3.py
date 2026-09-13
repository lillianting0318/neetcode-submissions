class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]

        for s, e in intervals[1:]:  # start from the second element
            # overlap
            if s <= res[-1][1]:
                # get the max end of two intervals
                res[-1][1] = max(res[-1][1], e)
            else:   # not overlap -> append as another interval
                res.append([s, e])
        
        return res
