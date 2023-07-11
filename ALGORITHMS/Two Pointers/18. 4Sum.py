class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sol = []
        nums= sorted(nums)
        for i in range(0, len(nums)-1):
            if (i>0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1, len(nums)):
                if (j>i+1 and nums[j] == nums[j-1]):
                    continue
                self.findPair(nums, target, i, j, sol)
        return sol
    
    def findPair(self, nums, target, i, j, sol):
        start = j + 1
        end = len(nums) - 1
        while start < end:
            s = [nums[start], nums[end], nums[i], nums[j]]
            
            if sum(s) == target:
                if s not in sol:
                    sol.append(s)
                end-=1
                start+=1
            elif sum(s) > target:
                end -= 1
                continue
            elif sum(s) < target:
                start += 1
                continue
        return sol
    

o = Solution()
x = o.fourSum(nums=[2,2,2,2,2], target = 8)
print(x)