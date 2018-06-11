class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in range(12):
            for j in range(60):
                s = str(bin(i)[2:])+str(bin(j)[2:])
                a = str(i)
                if len(str(j))<2:
                    b = "0"+str(j)
                else:
                    b = str(j)
                if s.count("1") == num:
                    res.append(a+":"+b)
        return res
        