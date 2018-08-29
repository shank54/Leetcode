class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        m = -float('inf')
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    a = (points[i][0]*(points[j][1]-points[k][1]))+(points[j][0]*(points[k][1]-points[i][1]))+(points[k][0]*(points[i][1]-points[j][1]))
                    a = abs(a)/2.0
                    m = max(m,a)
        return m