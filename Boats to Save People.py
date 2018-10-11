class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        i = 0
        j = len(people)-1
        people.sort()
        count = 0
        while i<=j:
            if people[j]+people[i]<=limit:
                i += 1
                j -= 1
                count += 1
            elif people[j]<=limit:
                count += 1
                j -= 1
        return count