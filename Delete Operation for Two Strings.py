class Solution(object):
    def minDistance(self, word1, word2):
        c = 0
        for i in word1:
            if i not in word2:
                word1 = word1.replace(i,"")
                c += 1
        
        for i in word2:
            if i not in word1:
                word2 = word2.replace(i,"")
                c += 1
        
        a = self.lSubSeq(word1,word2)
        
        return (len(word1)-a)+(len(word2)-a)+c
        
        
    def lSubSeq(self,s1,s2):
        l1 = len(s1)
        l2 = len(s2)
        arr = [[None]*(l2+1) for i in xrange(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i==0 or j==0:
                    arr[i][j] = 0
                elif s1[i-1]==s2[j-1]:
                    arr[i][j] = 1 + arr[i-1][j-1]
                else:
                    arr[i][j] = max(arr[i][j-1],arr[i-1][j])
        return arr[i][j]
            