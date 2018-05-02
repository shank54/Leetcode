class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f = [0]*len(cost)
        f[0] = cost[0]
        f[1] = cost[1]
        for i in range(2,len(cost)):
            f[i] = cost[i]+min(f[i-1],f[i-2])
        return min(f[len(cost)-1],f[len(cost)-2])