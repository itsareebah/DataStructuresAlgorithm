class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.sumsquare(n)
        fast = self.sumsquare(self.sumsquare(n))
        while slow != fast and fast!=1:
            slow = self.sumsquare(slow)
            fast = self.sumsquare(self.sumsquare(fast)) 
        return slow == 1

    def sumsquare(self, n):
        sum = 0
        while n!=0:
            rem = n%10
            sum += (rem**2)
            n =n // 10
        return sum

o = Solution()
x = o.isHappy(19)
print(x)