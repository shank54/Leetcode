class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper():
            return True
        if word.islower():
            return True
        if word.istitle():
            return True
        else:
            return False