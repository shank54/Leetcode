class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if not name and not typed:
            return True
        if not name or not typed:
            return False
        ntemp = []
        ttemp = []
        j = 0
        while j<len(name)-1:
            if name[j] != name[j+1]:
                ntemp.append([name[j],1])
                j += 1
            else:
                count = 1
                k = j+1
                while k<len(name) and name[j]==name[k]:
                    count += 1
                    k += 1
                ntemp.append([name[j],count])
                j += count
        if name[len(name)-1] == ntemp[len(ntemp)-1][0]:
            ntemp[len(ntemp)-1][1] += 1
        else:
            ntemp.append([name[len(name)-1],1])
        # print ntemp
        j = 0
        while j<len(typed)-1:
            if typed[j] != typed[j+1]:
                ttemp.append([typed[j],1])
                j += 1
            else:
                count = 1
                k = j+1
                while k<len(typed) and typed[j]==typed[k]:
                    count += 1
                    k += 1
                ttemp.append([typed[j],count])
                j += count
        if typed[len(typed)-1] == ttemp[len(ttemp)-1][0]:
            ttemp[len(ttemp)-1][1] += 1
        else:
            ttemp.append([typed[len(typed)-1],1])
        # print ttemp
        if len(ttemp)!=len(ntemp):
            return False
        for i in range(len(ntemp)):
            if ntemp[i][0] != ttemp[i][0]:
                return False
            else:
                if ntemp[i][1]>ttemp[i][1]:
                    return False
        return True