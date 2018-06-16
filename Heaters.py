class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        left = [float('inf')]*len(houses)
        right = [float('inf')]*len(houses)
        i = 0
        j = 0
        while i < len(houses) and j < len(heaters):
            if houses[i] <= heaters[j]:
                right[i] = heaters[j] - houses[i]
                i += 1
            else:
                j += 1        
        i = len(houses)-1
        j = len(heaters)-1
        while i>=0 and j >=0:
            if houses[i] >= heaters[j]:
                left[i] = houses[i]-heaters[j]
                i -= 1
            else:
                j -= 1
        res = [0]*len(houses)
        i = 0
        while i<len(res):
            res[i] = min(left[i],right[i])
            i += 1
        return max(res)