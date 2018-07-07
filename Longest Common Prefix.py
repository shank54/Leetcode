class Node:
    def __init__(self):
        self.d = dict()
        self.isEnd = False

class Solution(object):
    def __init__(self):
        self.root = Node()
        
    def insert(self,word):
        start = self.root
        for i in word:
            if i not in start.d:
                start.d[i] = Node()
            start = start.d[i]
        start.isEnd = True
        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i in strs:
            self.insert(str(i))
        
        start = self.root
        k = 0
        res = ""
        tmp = min(strs)
        while len(start.d)<2 and k<len(tmp):
            if not tmp:
                break
            i = str(tmp[k])
            if str(i) not in start.d:
                break
            start = start.d[str(i)]
            k += 1
            res += i
        return res