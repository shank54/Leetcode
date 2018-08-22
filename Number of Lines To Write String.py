class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        width = 0
        l = 0
        i = 0
        while i<len(S):
            l = widths[ord(S[i])-ord('a')]
            width += l
            if width > 100:
                lines += 1
                width = l
            i += 1
        return [lines,width]