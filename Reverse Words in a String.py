class Solution(object):
    def reverseWords(self, s):
        l = s.split()[::-1]
        return " ".join(l)