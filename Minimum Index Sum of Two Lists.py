class Solution(object):
    def findRestaurant(self, list1, list2):
        i = 0 
        m = float('inf')
        k = list()
        for i in list1:
            j = 0
            l = 0
            if i in list2:
                j = list1.index(i)
                l = list2.index(i)
                if j+l<=m:
                    m = j+l
                    k.append(i)
        return k