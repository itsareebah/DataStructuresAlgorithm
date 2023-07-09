class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy, sell = 0, 1
        while buy < sell and sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return profit
    

o = Solution()
x = o.maxProfit([7,1,5,3,6,4])
print(x)