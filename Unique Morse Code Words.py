class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        tmp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        d = dict()
        for i in words:
            s = ""
            for j in i:
                s += tmp[ord(j)-ord('a')]
            d.setdefault(s,0)
            d[s] += 1
        return len(d)
        