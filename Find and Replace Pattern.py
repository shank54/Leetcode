class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(words)):
            d = dict()
            d1 = dict()
            flag = 0
            for j in range(len(pattern)):
                if words[i][j] not in d1:
                    d1[words[i][j]] = pattern[j]
                else:
                    if pattern[j] != d1[words[i][j]]:
                        flag = 1
                        break
                if pattern[j] not in d:
                    d[pattern[j]] = words[i][j]
                else:
                    if words[i][j] != d[pattern[j]]:
                        flag = 1
                        break
            if flag == 0:
                res.append(words[i])
        return res
                        