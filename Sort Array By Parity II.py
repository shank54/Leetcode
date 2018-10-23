class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        res = [0]*len(even+odd)
        i = 0
        k = 0
        while i<len(even):
            res[k] = even[i]
            k += 2
            i += 1
        i = 0
        k = 1
        while i<len(odd):
            res[k] = odd[i]
            k += 2
            i += 1
        return res