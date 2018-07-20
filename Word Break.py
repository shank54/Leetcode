class Node:
    def __init__(self):
        self.d = dict()
        self.isEnd = False
class Solution(object):
    def __init__(self):
        self.root = Node()
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        for i in wordDict:
            self.insertWords(i)
        
        bol = [False]*len(s)
        for i in range(len(s)):
            if i==0 or bol[i-1]:
                self.fit(s,i,bol,self.root)
        return bol[len(s)-1]
        
        
    
    def insertWords(self,word):
        start = self.root
        for i in word:
            if i not in start.d:
                start.d[i] = Node()
            start = start.d[i]
        start.isEnd = True
    
    
    def fit(self,s,i,bol,start):
        while i<len(s) and start!=None:
            if s[i] not in start.d:
                break
            start = start.d[s[i]]
            if start and start.isEnd:
                bol[i] = True
            i += 1
    
    
    
    