class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0:
            if upper-lower != 0:
                return [str(lower)+"->"+str(upper)]
            else:
                return [str(lower)]
        
        s = ""
        res = []
        if nums[0] > lower:
            print "here1"
            if nums[0]-lower == 1:
                s = str(lower)
            else:
                s = str(lower)+"->"+str(nums[0]-1)
            res.append(s)
            
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > 1:
                print "here2"
                if nums[i]-nums[i-1] == 2:
                    s = str(nums[i-1]+1)
                else:
                    s = str(nums[i-1]+1)+"->"+str(nums[i]-1)
                res.append(s)
                
        if nums[-1] < upper:
            print "here3"
            if upper - nums[-1] == 1:
                s = str(upper)
            else:
                s = str(nums[-1]+1)+"->"+str(upper)
            res.append(s)
        
        return res
        