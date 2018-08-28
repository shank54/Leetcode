class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = dict()
        indx = 0
        for i in words:
            d.setdefault(i,[indx])
            d[i].append(indx)
            indx += 1
        l1 = d[word1]
        l2 = d[word2]
        m = float('inf')
        for i in range(len(l1)):
            for j in range(len(l2)):
                m = min(m,abs(l1[i]-l2[j]))
        return m