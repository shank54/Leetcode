class Solution(object):
    def arrangeCoins(self, n):
        low = 1
        high = n
        mid = low
        val = 0
        if n==0:
            return 0
        while low <= high:
            mid = low + (high-low)/2
            if (mid*(mid+1))/2 <= n:
                low = mid + 1
                val = mid
            else:
                high = mid - 1
        return val

