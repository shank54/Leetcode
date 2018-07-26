class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.replace("!","")
        paragraph = paragraph.replace("?","")
        paragraph = paragraph.replace("'","")
        paragraph = paragraph.replace(",","")
        paragraph = paragraph.replace(";","")
        paragraph = paragraph.replace(".","")
        temp = paragraph.split()
        d = dict()
        for i in temp:
            a = i.lower()
            if a not in banned:
                if a not in d:
                    d[a] = 1
                else:
                    d[a] += 1
        for i in sorted(d,key=d.get,reverse=True):
            return i