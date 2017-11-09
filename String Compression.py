class Solution(object):
    def compress(self, chars):
        i = 0
        m = 0
        indx = 0
        while i<len(chars):
            j = i+1
            chars[indx] = chars[i]
            indx += 1
            c = 1
            while j<len(chars) and chars[j] == chars[i]:
                c += 1
                j += 1
            if c>1:
                l = len(str(c))
                m = l
                x = 0
                while l>0:
                    chars[indx] = str(c)[x]
                    indx += 1
                    l -= 1
                    x += 1
            i = j
        return indx
        