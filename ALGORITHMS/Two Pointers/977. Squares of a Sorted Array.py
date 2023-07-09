class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [0 * len(nums)-1]
        ind = len(nums) - 1
        s, e = 0, len(nums) - 1
        while s < e:
            ps = nums[s] * nums[s]
            pe = nums[e] * nums[e]

            if ps > pe:
                arr[ind] = ps
                s += 1
            else:
                arr[ind] = pe
                e -= 1
            ind -= 1
        return arr



            


o = Solution()
print(o.sortedSquares([-5, -3, 0, 2, 4]))