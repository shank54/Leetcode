class Node:
    def __init__(self):
        self.d = dict()
        self.isEnd = False
        
class Solution(object):
    def __init__(self):
        self.root = Node()
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        for i in words:
            self.insertTrie(i)
        
        res = [False]*(len(S))
        for i in range(len(S)):
            start = self.root
            temp = i
            for j in range(i,len(S)):
                if str(S[j]) not in start.d:
                    break
                start = start.d[S[j]]
                if start.isEnd:
                    temp = j+1
            res[i:temp] = [True]*(temp-i)
        ans = []
        i = 0
        while i<len(S):
            if res[i] and (i==0 or not res[i-1]):
                ans.append("<b>")
            ans.append(S[i])
            if res[i] and (i==len(S)-1 or not res[i+1]):
                ans.append("</b>")
            i += 1
        return "".join(ans)
            
        
    
    def insertTrie(self,word):
        start = self.root
        for i in word:
            if i not in start.d:
                start.d[i] = Node()
            start = start.d[i]
        start.isEnd = True
                