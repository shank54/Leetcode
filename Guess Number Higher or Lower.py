# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l = 1
        h = n
        while l<=h:
            m = l+(h-l)/2
            if guess(m)==0:
                return m
            elif guess(m)==1:
                l = m+1
            else:
                h = m-1