class Solution(object):
    def anagramMappings(self, A, B):
        d = dict()
        for i in range(len(B)):
            if B[i] not in d:
                d[B[i]] = i
            else:
                d[B[i]] = i
        l = []
        for i in A:
            l.append(d[i])
        return l
            
