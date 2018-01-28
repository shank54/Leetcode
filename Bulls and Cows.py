class Solution(object):
    def getHint(self, secret, guess):
        #build the dicts
        d1 = self.builddict(secret)
        d2 = self.builddict(guess)
        #compare the common dict elements lists 
        a,b = 0,0
        for i in d2:
            c,d = 0,0
            if i in d1:
                #find common indices
                c = len(list(set(d1[i])&set(d2[i])))
                d = min(len(d1[i]),len(d2[i]))-c
            a += c
            b += d
        return str(a)+"A"+str(b)+"B"
    
    def builddict(self,s):
        d = dict()
        for i in range(len(s)):
            if str(s[i]) not in d:
                d.setdefault(str(s[i]),[])
                d[str(s[i])].append(i)
            else:
                d[str(s[i])].append(i)
        return d
                