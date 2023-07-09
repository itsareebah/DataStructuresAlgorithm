class Solution(object):
    def findAnagrams(self, s2, s1):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        start, char, match, l= 0,{}, 0, []
        for ch in s1:
            if ch not in char.keys():
                char[ch] = 0
            char[ch] += 1

        for end in range(len(s2)):
            if s2[end] in char.keys():
                char[s2[end]] -= 1
                if char[s2[end]] == 0:
                    match += 1
            
            if match == len(char.keys()):
                l.append(start)
            if end - start + 1 > len(s1):
                if s2 [start] in char.keys():
                    if char[s2[start]] == 0 :
                        match -= 1
                    char[s2[start]] += 1
                start += 1

        return l
    