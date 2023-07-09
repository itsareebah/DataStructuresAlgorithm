class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start, maxm, rep, char = 0, 0, 0, {}
        for end in range(len(s)):
            if s[end] not in char.keys():
                char[s[end]] = 0
            char[s[end]] += 1
            rep = max(rep, char[s[end]])
            if end - start + 1 - rep > k:
                char[s[start]] -= 1
                start += 1
                rep -= 1
            maxm = max(maxm, end - start + 1)
        return maxm


