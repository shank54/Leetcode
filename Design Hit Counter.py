class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = [0]*300
        self.hits = [0]*300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        indx = timestamp%300
        if self.time[indx] != timestamp:
            self.time[indx] = timestamp
            self.hits[indx] = 1
        else:
            self.hits[indx] += 1
        
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        count = 0
        for i in range(len(self.time)):
            if timestamp - self.time[i]<300:
                count += self.hits[i]
        return count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)