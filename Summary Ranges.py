class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:
            return []
        s = []
        l = []
        for i in range(len(nums)-1):
                s.append(nums[i+1]-nums[i])
        s.append(2)
        i = 0
        while i<len(s):
            ans = ""
            if s[i]==1:
                ans += str(nums[i])
                j = i+1
                while j<=len(s)-1 and s[j]==1:
                    s[j]=0
                    j += 1
                ans += "->"+str(nums[j])
                i = j+1
            else:
                ans += str(nums[i])
                i += 1
            l.append(ans)
        return l