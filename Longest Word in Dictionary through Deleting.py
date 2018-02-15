class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        mx = 0
        ans = ""
        for i in d:
            k = 0
            #check subsequence
            for char in range(len(s)):
                if k<len(i) and s[char] == i[k]:
                    k += 1
            if k==len(i):
                if k>mx or (k==mx and i<=ans):
                    mx = k
                    ans = i
        return ans