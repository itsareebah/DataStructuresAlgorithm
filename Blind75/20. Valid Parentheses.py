class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if not stack:
                    return 0
                elif i == ']' and stack[-1] =='[':
                    stack.pop()
                elif i == ')' and stack[-1] =='(':
                    stack.pop()
                elif i == '}' and stack[-1] =='{':
                    stack.pop()
                else:
                    return 0
        if stack:
            return 0
        return 1
    
o = Solution()
x = o.isValid('()[')
print(x)


                
             