class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        ans = 0
        for i in range(len(points)):
            d = dict()
            for j in range(len(points)):
                if i==j:
                    continue
                a = points[i][0] - points[j][0]
                b = points[i][1] - points[j][1]
                res = (a*a+b*b)**(0.5)
                if res not in d:
                    d[res] = 1
                else:
                    d[res] += 1
            for k in d:
                ans += d[k]*(d[k]-1)
        return ans
        