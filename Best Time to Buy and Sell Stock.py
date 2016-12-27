class Solution(object):
    def maxProfit(self, prices):
        n =sys.maxint
        m = 0
        l = len(prices)
        for i in range(0,l):
            n = min(n,prices[i])
            m = max(m,prices[i]-n)
        return m