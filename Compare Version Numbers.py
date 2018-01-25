class Solution(object):
    def compareVersion(self, version1, version2):
        l1 = version1.split(".")
        l2 = version2.split(".")
        a = len(l1)
        b = len(l2)
        if a==b:
            for i in range(a):
                if int(l1[i]) > int(l2[i]):
                    return 1
                elif int(l1[i]) < int(l2[i]):
                    return -1
            return 0
        elif a<b:
            for i in range(a):
                if int(l1[i]) > int(l2[i]):
                    return 1
                elif int(l1[i]) < int(l2[i]):
                    return -1
            if int(l2[-1]) == 0:
                return 0
            else:
                return -1
        else:
            for i in range(b):
                if int(l1[i]) > int(l2[i]):
                    return 1
                elif int(l1[i]) < int(l2[i]):
                    return -1
            if int(l1[-1]) == 0:
                return 0
            else:
                return 1