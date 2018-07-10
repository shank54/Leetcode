class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = " ".join(sentence)+" "
        indx = 0
        for i in range(rows):
            indx += cols
            if s[indx%len(s)] == " ":
                indx += 1
            else:
                while s[(indx-1)%len(s)] != " ":
                    indx -= 1
        return indx/len(s)