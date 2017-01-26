class Solution(object):
    def reverseVowels(self, s):
        a = 0
        s = list(s)
        b = len(s)-1
        c = "aeiouAEIOU"
        while a<b:
            while s[b] not in c and a<b:
                b -= 1
            while s[a] not in c and a<b:
                a += 1
            s[a],s[b]=s[b],s[a]
            a += 1
            b -= 1
        s = ''.join(s)
        return s
            
                
        