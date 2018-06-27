class Codec:
    def __init__(self):
        self.d = dict()
        self.count = 0
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if self.count not in self.d:
            self.count += 1
            self.d[self.count] = longUrl
        return "http://tinyurl.com/"+str(self.count)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        shortUrl = shortUrl.replace("http://tinyurl.com/","")
        return self.d[int(shortUrl)]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))