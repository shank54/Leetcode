class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxarr = [0]*len(arr)
        maxarr[0] = arr[0]
        for i in range(1,len(arr)):
            maxarr[i] = max(maxarr[i-1],arr[i])
        
        c = 0
        for i in range(len(arr)):
            if maxarr[i] == i:
                c += 1
        return c