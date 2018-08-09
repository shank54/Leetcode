# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        person = 0
        for i in range(1,n):
            if knows(person,i):
                person = i
        for i in range(n):
            if (i!= person and knows(person,i)) or (not knows(i,person)):
                return -1
        return person