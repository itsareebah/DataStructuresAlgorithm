class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        start, char, match = 0,{}, 0
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
                return 1 
            if end - start + 1 > len(s1):
                if s2 [start] in char.keys():
                    if char[s2[start]] == 0 :
                        match -= 1
                    char[s2[start]] += 1
                start += 1 

        return 1 if match == len(char.keys()) else 0
    

ob = Solution()
print(ob.checkInclusion(s1 = "trinitrophenylmethylnitramine", s2 =
"dinitrophenylhydrazinetrinitrophenylmethylnitramine"))