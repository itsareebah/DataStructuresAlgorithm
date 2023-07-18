class Solution(object):
    def canAttendAppointments(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        i = 1
        end = intervals[0][1]
        while i < len(intervals):
            if intervals[i][0] <= end:
                return False
            else:
                end = intervals[i][1]
            i += 1
        return True

o = Solution()
x = o.canAttendAppointments([[4,5], [2,3], [3,6], [5,7], [7,8]])
print(x)