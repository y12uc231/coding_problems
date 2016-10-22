

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = -1
        for i in prices:
            if min_price > i:
                min_price = i
            else:
                if (i - min_price) > max_profit:
                    max_profit = i - min_price
        return max_profit
