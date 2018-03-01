class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        i = 0
        j = 0
        l1 = list(S)
        l2 = list(T)
        tmp = 0
        for i in range(len(l1)):
            for j in range(i,len(l2)):
                if l2[j] == l1[i]:
                    l2[tmp],l2[j] = l2[j],l2[tmp]
                    tmp += 1
        return "".join(l2)
        