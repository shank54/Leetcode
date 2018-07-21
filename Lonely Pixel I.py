class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        col = [0]*len(picture[0])
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j] == "B":
                    col[j] += 1
        
        res = 0
        tmp = 0
        for i in range(len(picture)):
            count = 0
            for j in range(len(picture[i])):
                if picture[i][j] == "B":
                    count += 1
                    tmp = j
            if count == 1 and col[tmp]==1:
                res += 1
        return res