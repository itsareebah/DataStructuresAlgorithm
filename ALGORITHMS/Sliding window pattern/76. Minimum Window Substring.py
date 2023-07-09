class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        matched = 0
        minm = len(s)+1
        start, subs, ch = 0, -1, {}
        for i in t:
            if i not in ch:
                ch[i] = 0
            ch[i] += 1
        
        for end in range(len(s)):
            if s[end] in ch.keys():
                ch[s[end]] -= 1
                if ch[s[end]] >= 0:
                    matched += 1

            while matched == len(t):
                if end - start + 1 < minm:
                    minm = end - start + 1
                    subs = start
                if s[start] in ch.keys():
                    if ch[s[start]] == 0:
                        matched -= 1
                    ch[s[start]] += 1
                start += 1
        if minm > len(s):
            return ''
        return s[subs: subs+minm]


o = Solution()
x = o.minWindow('a', 'b')
print(x)