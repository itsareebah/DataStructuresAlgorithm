class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            forward = nums[i] >= 0
            fast = slow = i
            while True:
                slow = self.next(nums, forward, slow) # move to next index
                fast = self.next(nums, forward, fast) # move to next index

                if fast != -1:
                    fast = self.next(nums, forward, fast) # move again for fast - to double
                
                if slow == -1 or fast ==-1 or fast == slow: # if it breaks out of arr or goes 
                    break                                   # backward or finds a loop break
            if slow != -1 and fast == slow:  # return true as soon as i find a cycle
                return True
        return False

    def next(self, arr, forward, index):
        if(arr[index] >= 0) == forward: # if change in direction
            n = (index + arr[index]) % len(arr) # rounding
            n = n+len(arr) if n < 0 else n # if negative value
            if n == index: # single element loop
                return -1
            return n
        return -1  

