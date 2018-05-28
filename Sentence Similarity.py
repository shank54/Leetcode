class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1)!=len(words2):
            return False
        d = dict()
        for i in pairs:
            if i[0] not in d:
                d[str(i[0])] = [str(i[1])]
            else:
                d[str(i[0])].append(str(i[1]))
        i = 0
        while i<len(words1):
            if (str(words1[i]) in d and words2[i] in d[words1[i]]) or (str(words2[i]) in d and words1[i] in d[words2[i]]) or (str(words1[i]) == str(words2[i])):
                i += 1
            else:
                return False
        return True