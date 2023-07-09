class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fruit = {}
        wstart, maxlen = 0, 0
        for wend in range(len(fruits)):
            if fruits[wend] not in fruit:
                fruit[fruits[wend]] = 0
            fruit[fruits[wend]] += 1
        
            while len(list(fruit.keys())) > 2:
                fruit[fruits[wstart]] -= 1
                if fruit[fruits[wstart]] == 0:
                    del fruit[fruits[wstart]]
                wstart += 1
            maxlen = max(maxlen, wend - wstart + 1)

        return maxlen