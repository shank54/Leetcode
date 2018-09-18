class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        q = []
        q.append([beginWord,1])
        vis = {}
        vis[beginWord] = 1
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        wordList = set(wordList)
        while q:
            word,length = q.pop(0)
            if word == endWord:
                return length
            for w in range(len(word)):
                for alpha in alphabets:
                    if alpha != word[w]:
                        new = word[:w]+alpha+word[w+1:]
                        if new not in vis and new in wordList:
                            templength = length+1
                            q.append([new,templength])
                            vis[new] = 1
        return 0
    