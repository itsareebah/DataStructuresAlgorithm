class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = [1] * len(nums)
        val = 1
        
        for i in range(len(nums)):
            print(prod[i], val)
            prod[i] *= val
            val *= nums[i]
        
        val = 1
        print('he')
        for j in range(len(nums)-1, -1, -1):
            print(prod[j], 'alal')
            prod[j] *= val
            val *= nums[j]
        return prod
    
o = Solution()
x = o.productExceptSelf([1,2,0,4])
print(x)
