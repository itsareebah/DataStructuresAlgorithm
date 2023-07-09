class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        c = {}
        ans = []
        for i in nums:
            if i not in c:
                c[i] = 0
            c[i] += 1

        top = sorted(c.values(), reverse=True)[:k]
        for i in top:
            for j in c.keys():
                if c[j] == i:
                    c[j] = 0
                    ans.append(j)
                    break
        return ans

o = Solution()
x = o.topKFrequent([1, 2], 2)
print(x)
