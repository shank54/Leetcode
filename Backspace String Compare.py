class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        tempS = []
        tempT = []
        i = 0
        while i<len(S):
            if S[i] != "#":
                tempS.append(S[i])
            else:
                if tempS:
                    tempS.pop()
            i += 1
        i = 0
        while i<len(T):
            if T[i] != "#":
                tempT.append(T[i])
            else:
                if tempT:
                    tempT.pop()
            i += 1
        return tempS == tempT