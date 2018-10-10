class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in A:
            if i%2 == 0:
                arr.append(i)
        for i in A:
            if i%2 != 0:
                arr.append(i)
        return arr