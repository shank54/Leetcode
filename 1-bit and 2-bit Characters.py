class Solution(object):
    def isOneBitCharacter(self, bits):
        # iterate from index 1 and if previous index is 1 then jump the pointer 2 indices else jump 1 index
        i = 0
        l = len(bits)
        while i<l-1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i==l-1
            
        