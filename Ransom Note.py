class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d = dict();
        e = dict();
        c = 0
        x = 0
     
        for c in magazine:
            e.setdefault(c,0)
            e[c]+=1
        
        
        for key in ransomNote :
            
            if key not in e :
                return False
            
            if e[key]==0:
                return False
            e[key] -= 1
        
        return True