class Solution(object):
    def findTheDifference(self, s, t):
        a = 0 
        b = 0
        for i in s:
            a +=ord(i)
        for i in t:
            b += ord(i)
        return chr(b-a)