class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        nums= sorted(nums)
        for i in range(0, len(nums)):
            if (i>0 and nums[i] == nums[i-1]):
                continue
            self.findPair(nums, -nums[i], i+1, sol)
        return sol
    
    def findPair(self, nums, target, start, sol):
        e = len(nums) - 1
        while start < e:
            
            if nums[start] + nums[e] == target:
                if [nums[start], nums[e], -target] not in sol:
                    sol.append()
                e-=1
                start+=1
            elif nums[start] + nums[e] > target:
                e -= 1
                continue
            elif nums[start] + nums[e] < target:
                start += 1
                continue
           
        return sol
        
o = Solution()
x = o.threeSum([-1,0,1])
print(x)