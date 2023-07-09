import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # time complexity reduce krni h 
        wmax, win = [], collections.deque() 
        for wend in range(len(nums)):
            win.append(nums[wend])
            if len(win) >= k:
                wmax.append(max(list(win)))
                win.popleft()
        return wmax