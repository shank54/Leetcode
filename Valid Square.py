class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        a1 = self.dist(p1,p2)
        a2 = self.dist(p1,p3)
        a3 = self.dist(p1,p4)
        a4 = self.dist(p2,p3)
        a5 = self.dist(p2,p4)
        a6 = self.dist(p3,p4)
        l = [a1,a2,a3,a4,a5,a6]
        d = dict()
        for i in l:
            d.setdefault(i,0)
            d[i] += 1
        if len(d)==2 :
            flag = 0
            for i in d:
                if (d[i]==2 or d[i]==4):
                    flag = 0
                else:
                    flag = 1
            if flag==0:
                return True
            else:
                return False
        else:
            return False
        
        
    def dist(self,a,b):
        x = (b[0]-a[0])**2
        y = (b[1]-a[1])**2
        return float((x+y)**(0.5))