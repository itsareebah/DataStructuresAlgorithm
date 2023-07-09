class Solution(object):
    # complexity - O(n)
    def findMaxAverage(self, nums, k):
        sum, wStart= 0.0, 0
        result = []
        for wEnd in range(0, len(nums)):
            sum += nums[wEnd]

            if wEnd >= k-1:
                x = float(sum/k)
                result.append(x)

                sum -= nums[wStart]
                wStart += 1
        return max(result)
                

                

            