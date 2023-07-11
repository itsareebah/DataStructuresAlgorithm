class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, result, val= 0, 0, 1
        for end in range(len(nums)):
            val *= nums[end]
            while val >= k and start < len(nums):
                val = val / nums[start]
                start += 1
            if val < k:
                result += end - start + 1 # ye hamesha 2 ya 1 range m hoga
        return result


o = Solution()
x = o.numSubarrayProductLessThanK(nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3], k = 19)
print(x)