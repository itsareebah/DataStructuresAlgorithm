class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return 1
        specialchar = "~`!@#$%^&*()-=_+[{]|}\/:<>,.?;''\"\" "
        s = ''.join(x.lower() for x in s if x not in specialchar)
        p1, p2 = 0, len(s)-1
        while p1<=p2:
            if s[p1] != s[p2]:
                return 0
            p1+=1
            p2-=1
        return 1
    
o = Solution()
x = o.isPalindrome('A man, a plan, a canal: Panama')
print(x)