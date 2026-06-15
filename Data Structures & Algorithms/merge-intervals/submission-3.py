class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        if len(intervals)<= 1: 
            return intervals
        res = []
        l,r = intervals[0]

        for i in range(1,len(intervals)):
            if r < intervals[i][0]:
                res.append([l,r])
                l,r = intervals[i]
            else:
                l = min(l, intervals[i][0])
                r = max(intervals[i][1],r)

        res.append([l,r])
        return res
