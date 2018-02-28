class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flag = 0
        for i in range(len(matrix)):
            l = matrix[i]
            a = self.bs(0,len(l)-1,l,target)
            if a==-1:
                flag = 1
            else:
                flag = 2
                break
        if flag == 2:
            return True
        else:
            return False
        
    def bs(self,l,r,arr,k):
        while l<=r:
            m = l+(r-l)/2
            if arr[m] == k:
                return m
            elif k<arr[m]:
                r = m-1
            else:
                l = m+1
        return -1