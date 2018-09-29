class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        stk = []
        stk.append(0)
        temp = [0]*len(rooms)
        temp[0] = 1
        while stk:
            t = stk.pop()
            for i in rooms[t]:
                if temp[i] != 1:
                    temp[i] = 1
                    stk.append(i)
        for i in temp:
            if i == 0:
                return False
        return True                  