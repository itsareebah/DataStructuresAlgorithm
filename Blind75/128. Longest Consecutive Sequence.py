class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max, maxm = 0, 0
        nums = set(nums)
        for i in nums:
            if i - 1 not in nums:
                e = 1
                while i + e in nums:
                    e += 1
                local_max = e
                print(local_max, i)
                maxm = max(local_max, maxm)
        return maxm

o = Solution()
x = o.longestConsecutive([0,3,7,2,5,0,4,6,0,1])
print(x)
            
            
            