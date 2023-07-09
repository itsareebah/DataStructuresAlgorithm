class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = {}
        for i in words:
            if i not in d:
                d[i] = 0
            d[i] += 1

        