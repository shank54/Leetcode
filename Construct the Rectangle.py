class Solution(object):
    def constructRectangle(self, area):
        min  = sys.maxint
        m = area
        a = 0
        b = 0
        i = 1
        diff = 0
        if area==1:
            return [1,1]
        while i*i<=(area):
            if area%i==0:
                diff = abs((m/i)-i)
            if diff<min:
                min = diff
                a = m/i
                b = i
            i += 1
        return [a,b]
                
        