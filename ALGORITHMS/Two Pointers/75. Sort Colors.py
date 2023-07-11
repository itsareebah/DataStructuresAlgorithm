class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # write insertion sort or
        start, end, iter= 0, len(nums)-1, 0
        while iter <= end:
            if nums[iter] == 0:
                nums[iter], nums[start] = nums[start], nums[iter]
                start += 1
                iter += 1
            elif nums[iter] == 2:
                nums[iter], nums[end] = nums[end], nums[iter]
                end -= 1
            else:
                iter += 1
            
o = Solution()
x = [2,0,2,1,1,0]
o.sortColors(x)
print(x)
        

             