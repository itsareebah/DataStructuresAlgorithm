class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        
        ans = []
        intervals = firstList + secondList
        intervals.sort()
        i = 1
        start, end = intervals[0][0], intervals[0][1]
        while i < len(intervals):
            if intervals[i][0] <= end:
                ans.append([intervals[i][0], min(intervals[i][1], end)])
                end = max(end, intervals[i][1])
                start = min (start, intervals[i][0])
            else:
                start = intervals[i][0]
                end = intervals[i][1]
            i += 1
        return ans
    
o = Solution()
x = o.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])
print(x)