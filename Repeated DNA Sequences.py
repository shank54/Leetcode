class Solution(object):
    def findRepeatedDnaSequences(self, s):
        d = dict()
        news = ""
        l = []
        for i in range(len(s)):
            if i+10<=len(s):
                news = s[i:i+10]
                if news not in d:
                    d[news] = 1
                else:
                    if news not in l:
                        l.append(news)
        return l
        