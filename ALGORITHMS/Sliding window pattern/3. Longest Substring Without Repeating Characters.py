class Solution(object):
    def lengthOfLongestSubstring(self, string):
        start = 0
        maxv = 0
        las_pos = {}
        for end in range(len(string)):
            if string[end] in las_pos.keys():
                start = max(start, las_pos[string[end]]+1)
            las_pos[string[end]] = end
            maxv = max(maxv, end - start +1)
        return maxv 
    