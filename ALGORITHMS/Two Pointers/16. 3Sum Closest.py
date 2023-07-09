class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m = float('inf')
        nums= sorted(nums)
        for i in range(0, len(nums)):
            start = i+1
            end = len(nums) - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if target - s == 0:
                    return s
                if target - s > 0:
                    start += 1
                else:
                    end -= 1
                m = target - s if min(abs(target-s), abs(m)) == abs(target - s) else m
        return target - m
        
        
o = Solution()
x = o.threeSumClosest([1, 1, 1, 0], 100)
print(x)