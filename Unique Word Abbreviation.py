class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = dict()
        for i in dictionary:
            if len(i)<=2:
                continue
            else:
                s = i[0]+str(len(i)-2)+i[-1]
            if s not in self.d:
                self.d[s] = [i]
            else:
                self.d[s].append(i)
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abb = word
        if len(word)>2:
            abb = word[0]+str(len(word)-2)+word[-1]
        
        if abb in self.d:
            if len(self.d[abb]) == 1:
                if self.d[abb][0] == word:
                    return True
                else:
                    return False
            else:
                return False
        return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)