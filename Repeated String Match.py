class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        res = ""
        count = 0
        while len(res)<len(B):
            res += A
            count += 1
            if B in res:
                return count
        res += A
        if B in res:
            return count + 1
        return -1
            