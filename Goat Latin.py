class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = ["a","e","i","o","u","A","E","I","O","U"]
        temp = S.split()
        for i in range(len(temp)):
            if temp[i][0] in vowel:
                temp[i] = temp[i]+"ma"+("a")*(i+1)
            else:
                t = temp[i][0]
                temp[i] = temp[i][1:]+t+"ma"+("a")*(i+1)
        return " ".join(temp)