class Solution(object):
    def longestOnes(self, s, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxlen, start, rep = 0, 0, 0
        for end in range(len(s)):
            if s[end] == 1:
                rep += 1

            if(end - start + 1 - rep) > k:
                print(end, start, rep)
                if s[start] == 1:
                    rep -= 1
                start += 1
            maxlen = max(maxlen, end - start + 1)
        return maxlen
    
o = Solution()
print(o.longestOnes([1,0,1,0,1,1,0,0,0], 2))
# [1,0,1,0,1,1,0,0,0]