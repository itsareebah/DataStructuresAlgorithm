class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        start, end = 0, n -1
        while start < end and arr[start] <= arr[start + 1]:
            start += 1

        if start == end:
            return 0
        
        while end > 0 and arr[end] >= arr[end - 1]:
            end -= 1

        minv = min(end, abs(n - start - 1))
        
        left, right = 0, end
        while left <= start and right < n:
            if arr[left] <= arr[right]:
                minv = min(minv, right - left - 1)
                left += 1
            else:
                right += 1 
        return minv

o = Solution()
x = o.findLengthOfShortestSubarray([22,37,59,16,42,32,29,53,9,55,29,3,4,1,49,17,
                                    37,31,27,45,33,24,54,51,32,51,54,31,36,53])
print(x)

