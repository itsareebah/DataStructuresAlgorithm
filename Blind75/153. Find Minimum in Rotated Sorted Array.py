class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            print(start, end)
            if nums[start] < nums[end]:
                return nums[start]
            
            mid = (start + end) // 2
            if mid>0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return 0
    
o = Solution()
x = o.findMin([3,4,5,1,2])
print(x)
            