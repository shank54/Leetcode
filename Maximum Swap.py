class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        m = num
        l = list(str(num))
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                l[i],l[j] = l[j],l[i]
                n = int("".join(l))
                if n>m:
                    m = n
                l[i],l[j] = l[j],l[i]
        return m