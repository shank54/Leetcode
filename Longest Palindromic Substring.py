class Solution(object):
    def longestPalindrome(self, s):
        m = 1
        le = len(s)
        l = 0
        h = 0
        st = 0
        for i in range(1,le):
            l = i-1
            h = i
            while l>=0 and h<le and s[l]==s[h]:
                if h-l+1>m:
                    st = l
                    m = h-l+1
                l -= 1
                h += 1
            l = i-1
            h = i+1
            while l>=0 and h<le and s[l]==s[h]:
                if h-l+1>m:
                    st = l
                    m = h-l+1
                l -= 1
                h += 1
        return s[st:st+m]
        