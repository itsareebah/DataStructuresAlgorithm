class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d, matched={}, 0
        if len(s) == len(t):
            for i in s:
                if i not in d:
                    d[i] = 0
                d[i] += 1
                
            for end in t:
                if end not in d.keys():
                    return 0
                d[end] -= 1
                if d[end] == 0:
                    matched += 1
            if matched == len(d.keys()):
                return 1
        return 0

o =Solution()
print(o.isAnagram(s = "anagram", t = "nagaram"))