class Solution(object):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # with sorted O(n)
    def groupAnagrams(self, strs):
        anagrams = {}
        
        for word in strs:
            count = sorted(list(c for c in word))            
            key = tuple(count) 
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())


class Solution1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # without using sorted function - O(n2)
        sol = []
        j = len(strs) - 1
        while j >= 0:
            dc = {}
            ans = []
            for k in strs[j]:
                if k not in dc:
                    dc[k] = 0
                dc[k] += 1
            i = len(strs) - 1

            while i >= 0:
                matched = 0
                d = dc.copy()
                if len(strs[j]) == len(strs[i]):
                    for end in strs[i]:
                        if end not in d.keys():
                            continue
                        d[end] -= 1
                        if d[end] == 0:
                            matched += 1
                    if matched == len(d.keys()):
                        if strs[i] not in ans:
                            ans.append(strs[i])
                i -= 1
            if ans not in sol:
                sol.append(ans)
            j-=1
        return sol


o = Solution()
x = o.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
print(x)