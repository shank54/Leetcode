class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand)%W != 0:
            return False
        d = dict()
        for i in hand:
            d.setdefault(i,0)
            d[i] += 1
        count = 0
        while count<len(hand):
            temp = []
            mini = min(d)
            while len(temp)<W:
                count += 1
                if mini in d:
                    temp.append(mini)
                    d[mini] -= 1
                    if d[mini] == 0:
                        del d[mini]
                    mini += 1
                else:
                    break
            if len(temp)<W:
                return False
        return True
            