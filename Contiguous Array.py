class Solution(object):
    def findMaxLength(self, nums):
        d = dict()
        s = 0
        m_len = 0
        nums1 = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums1[i] = -1
            else:
                nums1[i] = nums[i]
        for i in range(len(nums1)):
            s += nums1[i]
            if s == 0:
                m_len = i+1
            if s in d:
                m_len = max(m_len,i-d[s])
            else:
                d[s] = i
        return m_len
        