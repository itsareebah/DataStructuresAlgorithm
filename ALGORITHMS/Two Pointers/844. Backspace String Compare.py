class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p1, p2 = len(s)-1, len(t)-1
        while p1 >= 0 and p2 >= 0:
            i = self.valid_index(s, p1)
            j = self.valid_index(t, p2)

            if i < 0 and j < 0:
                return 1
            if i < 0 or j < 0:
                return 0
            print(i, j)
            if s[i] != t[j]:
                return 0 
            p1 = i - 1
            p2 = j - 1
        return 1
        
    def valid_index(self, string, ptr):
        bs = 0
        while (ptr >= 0):
            if string[ptr] == '#':
                bs += 1
            elif bs > 0:
                bs -= 1
            else:
                break
            ptr -= 1
        return ptr



o = Solution()
x = o.backspaceCompare(s = "bbbextm", t = "bbb#extm")
print(x)


