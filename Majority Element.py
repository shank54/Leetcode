class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        srt = sorted(count,key=count.get,reverse=True)
        return srt[0]
        