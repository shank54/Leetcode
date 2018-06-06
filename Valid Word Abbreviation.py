class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if not word or not abbr:
            return False
        i = 0
        j = 0
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        while i<len(word) and j<len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            if abbr[j] not in digits[1:]:
                return False
            tmp = j
            while j<len(abbr) and abbr[j] in digits:
                j += 1
            num = int(abbr[tmp:j])
            i += num
        return i == len(word) and j == len(abbr)