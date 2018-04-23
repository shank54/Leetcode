class Node():
    def __init__(self):
        self.d = dict()
        self.isEnd = False
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()        
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        start = self.root
        for i in word:
            if i not in start.d:
                start.d[i] = Node()
            start = start.d[i]
        start.isEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        start = self.root
        for w in word:
            if w not in start.d:
                return False
            start = start.d[w]
        return start.isEnd
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        start = self.root
        for p in prefix:
            if p not in start.d:
                return False
            start = start.d[p]
        if len(start.d)>0 or start.isEnd:
            return True
        else:
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)