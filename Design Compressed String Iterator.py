class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.s = compressedString
        self.char = 0
        self.num = 0
        self.count = 0
        

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.count -= 1
            return self.s[self.char]
        return " "
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.char > len(self.s):
            return False
        if self.count == 0:
            self.char = self.num
            tmp = self.char+1
            a = ""
            while tmp<len(self.s) and self.s[tmp].isdigit():
                a += self.s[tmp]
                tmp += 1
            self.num = tmp
            if a!="":
                self.count = int(a)
        return self.count > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()