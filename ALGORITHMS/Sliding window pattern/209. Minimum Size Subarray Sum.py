class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # complexity - O(n)
        wsum, wstart, minlen = 0, 0, float('inf')
        for wend in range(len(nums)):
            wsum += nums[wend]
            while wsum >= target:
                minlen = min(minlen, wstart - wend + 1)
                wsum -= nums[wstart]
        if minlen == float("inf"):
            return 0
        return minlen


            
                
                
            



