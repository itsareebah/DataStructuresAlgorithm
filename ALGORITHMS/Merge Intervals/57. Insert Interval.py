class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        intervals.append(newInterval)
        intervals.sort()
        i = 0
        start, end = intervals[0][0], intervals[0][1]
        while i < len(intervals):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                ans.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            i += 1
        ans.append([start, end])
        return ans
    