class Node:
    def __init__(self):
        self.d = dict()
        self.isEnd = False
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        start = self.root
        l = len(word)
        if l not in start.d:
            start.d[l] = [word]
        else:
            start.d[l].append(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        start = self.root
        if not word:
            return False
        if "." not in word:
            if len(word) in start.d:
                if word in start.d[len(word)]:
                    return True
                else:
                    return False
            else:
                return False
        if len(word) in start.d:
            for i in start.d[len(word)]:
                flag = 1
                for j in range(len(word)):
                    if word[j]!=i[j] and word[j]!=".":
                        flag = 0
                        break
                if flag:
                    return True
        return False
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)